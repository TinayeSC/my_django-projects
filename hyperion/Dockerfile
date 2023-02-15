FROM pypy:latest
RUN pip install django
RUN source env/bin/activate 
WORKDIR /app
COPY . /app
CMD python manage.py runserver