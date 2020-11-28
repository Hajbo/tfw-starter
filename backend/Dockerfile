FROM python:3.9.0-buster

RUN apt-get update && \
    apt-get upgrade -y &&\
    apt-get install -y git

RUN useradd -ms /bin/bash startr

ENV STARTRDIR=/srv/startr

COPY . /srv/startr
WORKDIR $STARTRDIR

RUN python3 -m pip install -r requirements.txt &&\
    python3 -m pip install gunicorn==20.0.4 &&\
    chown -R startr:startr ./ &&\
    chmod a+x boot.sh

ENV TFW_STARTER_WORKING_DIRECTORY=/tmp/workdir          \
    TFW_STARTER_SOURCE_DIRECTORY="$STARTRDIR/avatao_startr/tfw" \
    FLASK_APP=startr.py \
    FLASK_ENV=production

USER startr
EXPOSE 5000
CMD ["./boot.sh"]