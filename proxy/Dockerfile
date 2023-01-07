FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./default.conf /etc/nginx/conf.d/default.conf

USER root

RUN mkdir -p /vol/static
RUN chmod 775 /vol/static

USER nginx 