FROM python:3

LABEL authors="Heattehnik"

WORKDIR /app

COPY ./requirements.txt  /app/

RUN pip install -r requirements.txt

COPY . .

CMD sh -c 'python manage.py migrate && \
           python manage.py loaddata fixtures/converter.json && \
           python manage.py runserver 0.0.0.0:8000'