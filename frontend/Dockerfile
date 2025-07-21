# 1. Билд-стейдж
FROM node:20-alpine AS builder

WORKDIR /app

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
