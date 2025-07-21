# 1. Билд-стейдж
FROM node:20-bullseye AS builder

WORKDIR /app

# Установим esbuild для Debian (опционально, но обычно не требуется)
# RUN apt-get update && apt-get install -y esbuild

COPY . .

RUN npm install
RUN npm run build

# 2. Сервер-стейдж (статический сервер)
FROM nginx:alpine

# Копируем собранные файлы во внутренний nginx www
COPY --from=builder /app/dist /usr/share/nginx/html

# Копируем кастомный nginx конфиг (опционально)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
