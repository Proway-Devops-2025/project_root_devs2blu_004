FROM nginx:1.25-alpine

RUN apk add --no-cache openssl \
    && mkdir -p /etc/nginx/certs \
    && openssl req -x509 -nodes -days 365 \
        -newkey rsa:2048 \
        -keyout /etc/nginx/certs/dev.key \
        -out /etc/nginx/certs/dev.crt \
        -subj "/C=BR/ST=SC/L=Florianopolis/O=Dev2Blu/OU=Edge/CN=localhost"

COPY containers/nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
