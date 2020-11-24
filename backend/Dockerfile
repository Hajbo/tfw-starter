FROM python:3.9.0-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY . /srv/app

WORKDIR /srv/app

ENV TFW_STARTER_WORKING_DIRECTORY=/tmp/workdir          \
    TFW_STARTER_SOURCE_DIRECTORY=/srv/app/avatao_startr/tfw
    
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]