FROM python:3



ADD settings.py /

WORKDIR /app
COPY . /app

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt 

WORKDIR / 
CMD python manage.py runserver