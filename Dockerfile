FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install psycopg2 && pip install django-crontab
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT