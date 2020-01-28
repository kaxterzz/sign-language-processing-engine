FROM joelogan/keras-tensorflow-flask-uwsgi-nginx-docker
RUN pip install socketio
COPY ./app /app