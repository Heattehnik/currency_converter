FROM python:3

LABEL authors="Heattehnik"

WORKDIR /app

COPY ./requirements.txt  /app/

RUN pip install -r requirements.txt

COPY . .
