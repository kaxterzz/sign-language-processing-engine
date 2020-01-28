FROM joelogan/keras-tensorflow-flask-uwsgi-nginx-docker
RUN python ins.py
COPY ./app /app