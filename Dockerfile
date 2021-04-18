# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.9-buster


RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

COPY nginx/nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY . /opt/app/

WORKDIR /opt/app

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends &&
pip install -r requirements.prod.txt && chown -R www-data:www-data /opt/app &&
  chmod -X /opt/app/start-server.sh

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
