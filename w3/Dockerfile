FROM python:3.7.0-alpine3.8
COPY /mysite /app
WORKDIR /app
RUN pip3 install Django
EXPOSE 8000
ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
