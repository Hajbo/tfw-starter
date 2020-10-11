FROM python:3

COPY . /usr/src/app

WORKDIR /usr/src/app

ENV TFW_STARTER_WORKING_DIRECTORY=/tmp/starter
ENV TFW_STARTER_SOURCE_DIRECTORY=/usr/src/app/tfw_base

RUN pip3 install -r requirements.txt

CMD ["python", "server.py"]