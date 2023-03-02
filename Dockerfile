FROM python:3.8-alpine3.12

ENV APP deployWatcher
WORKDIR /$APP

COPY ./requirements_docker.txt /$APP/requirements.txt
RUN pip install -r requirements.txt

COPY deployWatcher /$APP
COPY .env /$APP/.env

EXPOSE 5000

CMD python app.py