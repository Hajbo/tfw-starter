FROM python:3.9.0-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN useradd -ms /bin/bash startr

ENV VIRTUAL_ENV=/srv/startr
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR $VIRTUAL_ENV

COPY . /srv/startr
RUN python3 -m pip install -r requirements.txt
RUN chmod a+x boot.sh
RUN chown -R startr:startr ./

ENV TFW_STARTER_WORKING_DIRECTORY=/tmp/workdir          \
    TFW_STARTER_SOURCE_DIRECTORY="$VIRTUAL_ENV/avatao_startr/tfw" \
    FLASK_APP=startr.py \
    FLASK_ENV=production

USER startr

EXPOSE 5000

CMD ["./boot.sh"]