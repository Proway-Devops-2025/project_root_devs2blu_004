FROM nginx:1.25-alpine

COPY containers/frontend/nginx.conf /etc/nginx/conf.d/default.conf
COPY app/index.html /usr/share/nginx/html/index.html

EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
