FROM python:3.6.2-alpine3.6

ENV PYTHONUNBUFFERED 1
ENV APP_PATH /opt/book_task
WORKDIR $APP_PATH

COPY setup.py $APP_PATH
COPY manage.py $APP_PATH

# Packages
RUN apk add --no-cache libffi libressl libgcc protobuf mariadb-client-libs && \
    apk add --no-cache make gcc g++ python3-dev libffi-dev libressl-dev protobuf-dev mariadb-dev musl-dev --virtual .build-deps && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    pip3 install --no-cache-dir -e $APP_PATH[dev] && \
    apk del .build-deps

COPY ./book_task $APP_PATH/book_task
COPY ./book_task_app $APP_PATH/book_task_app

WORKDIR $APP_PATH
