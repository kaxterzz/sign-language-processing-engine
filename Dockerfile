FROM joelogan/keras-tensorflow-flask-uwsgi-nginx-docker
RUN pip install --upgrade setuptools
RUN pip install numpy
RUN pip install wheel
RUN pip install matplotlib
RUN pip install seaborn
RUN pip install sklearn
RUN pip install keras
RUN pip install opencv-python
RUN pip install tensorflow
RUN pip install tf-nightly
RUN pip install cloud-tpu-client
RUN pip install pillow
RUN pip install socketio
COPY ./app /app