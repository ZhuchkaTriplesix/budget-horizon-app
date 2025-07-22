import logging
import secrets
from contextvars import ContextVar
from typing import Final, Optional
from uuid import uuid1

import uvicorn
from fastapi import Depends, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from sqlalchemy.ext.asyncio import async_sessionmaker, async_scoped_session, AsyncSession
from starlette import status
from starlette.requests import Request
from starlette.responses import HTMLResponse

from src.configuration.app import App
from src import config
from src.database.core import engine
from src.database.logging import SessionTracker

logging.basicConfig(level=logging.INFO)

REQUEST_ID_CTX_KEY: Final[str] = "request_id"
_request_id_ctx_var: ContextVar[Optional[str]] = ContextVar(REQUEST_ID_CTX_KEY, default=None)


def get_request_id() -> Optional[str]:
    return _request_id_ctx_var.get()


app = App().app


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request_id = str(uuid1())

    # we create a per-request id such that we can ensure that our session is scoped for a particular request.
    # see: https://github.com/tiangolo/fastapi/issues/726
    ctx_token = _request_id_ctx_var.set(request_id)
    session = None

    try:
        session = async_scoped_session(async_sessionmaker(bind=engine, class_=AsyncSession), scopefunc=get_request_id)
        request.state.db = session()

        # we track the session
        request.state.db._ternhost_session_id = SessionTracker.track_session(
            request.state.db, context=f"api_request_ternhost"
        )

        response = await call_next(request)

        # If we got here without exceptions, commit any pending changes
        if hasattr(request.state, "db") and request.state.db.is_active:
            await request.state.db.commit()

        return response

    except Exception as e:
        # Explicitly rollback on exceptions
        try:
            if hasattr(request.state, "db") and request.state.db.is_active:
                await request.state.db.rollback()
        except Exception as rollback_error:
            logging.error(f"Error during rollback: {rollback_error}")

        # Re-raise the original exception
        raise e from None
    finally:
        # Always clean up resources
        if hasattr(request.state, "db"):
            # Untrack the session
            if hasattr(request.state.db, "_ternhost_session_id"):
                try:
                    SessionTracker.untrack_session(request.state.db._ternhost_session_id)
                except Exception as untrack_error:
                    logging.error(f"Failed to untrack session: {untrack_error}")

            # Close the session
            try:
                await request.state.db.close()
                if session is not None:
                    await session.remove()  # Remove the session from the registry
            except Exception as close_error:
                logging.error(f"Error closing database session: {close_error}")

        # Always reset the context variable
        _request_id_ctx_var.reset(ctx_token)


def get_current_username(credentials: HTTPBasicCredentials = Depends(HTTPBasic())) -> str:
    correct_username = secrets.compare_digest(credentials.username, "Reei")
    correct_password = secrets.compare_digest(credentials.password, "dnepr1")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/api/docs", response_class=HTMLResponse)
async def get_docs(username: str = Depends(get_current_username)) -> HTMLResponse:
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="docs")


if __name__ == "__main__":
    uvicorn.run(app, **config.uvicorn.dict())