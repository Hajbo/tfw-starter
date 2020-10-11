FROM avatao/controller:debian-buster

USER root
ENV PYTHONPATH="/usr/local/lib"      \
    TFW_PUB_PORT=7654                \
    TFW_PULL_PORT=8765               \
    TFW_AUTH_KEY="/tmp/tfw-auth.key" \
    CONTROLLER_PORT=5555

COPY ./controller/ /

CMD ["python3", "/opt/server.py"]
