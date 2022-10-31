FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 aws httpie chalice

COPY ./docker/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /code
COPY ./code /code

EXPOSE 8000

# ENTRYPOINT [ "chalice", "local", "--host=0.0.0.0", "--port=8000" ]