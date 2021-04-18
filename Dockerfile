FROM python:3.9-buster

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /opt/app/

RUN chmod 755 /opt/app/start-server.sh

RUN pip install -r requirements.prod.txt

STOPSIGNAL SIGTERM

ENTRYPOINT ["sh", "/opt/app/start-server.sh"]
