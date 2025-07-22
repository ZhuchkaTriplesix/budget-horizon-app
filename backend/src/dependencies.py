from typing import Annotated

from fastapi import Depends
from src.schemas import User
from src.security.security import Security

VUser = Annotated[User, Depends(Security().session_user_verify)]