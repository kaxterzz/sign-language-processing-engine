FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN pip install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate
RUN python ins.py
