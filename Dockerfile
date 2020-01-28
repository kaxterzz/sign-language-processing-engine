FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN pip install virtualenv
RUN pip install virtualenvwrapper
RUN virtualenv venv
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh"
RUN python ins.py
