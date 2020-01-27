FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

RUN python ins.py
