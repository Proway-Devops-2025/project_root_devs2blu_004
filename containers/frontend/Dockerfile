# -----------------------------------------------------------------------------
# Author: Adriano Machado <adriano@maxado.com.br>
# Description: Dockerfile for the static frontend served by Nginx.
# Last Updated: 2025-11-07
# -----------------------------------------------------------------------------
FROM nginx:1.25-alpine

COPY containers/frontend/nginx.conf /etc/nginx/conf.d/default.conf
COPY app/index.html /usr/share/nginx/html/index.html

EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
