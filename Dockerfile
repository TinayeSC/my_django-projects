FROM pypy:latest

RUN python -m venv /my_django/env

WORKDIR /app
COPY . /app
CMD python manage.py runserver