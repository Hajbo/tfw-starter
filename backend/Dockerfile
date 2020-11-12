FROM python:3

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY . /usr/src/app

WORKDIR /usr/src/app

ENV TFW_STARTER_WORKING_DIRECTORY=/tmp/starter          \
    TFW_STARTER_SOURCE_DIRECTORY=/usr/src/app/tfw
    
ENV TFW_STARTER_TEMPLATE_BASE="${TFW_STARTER_SOURCE_DIRECTORY}/base"                    \
    TFW_STARTER_LANGUAGE_TEMPLATES_DIRECTORY="${TFW_STARTER_SOURCE_DIRECTORY}/starters" \
    TFW_STARTER_JINJA_TEMPLATES_DIRECTORY="${TFW_STARTER_SOURCE_DIRECTORY}/templates"

ENV TFW_STARTER_DOCKERFILE_SOURCE="${TFW_STARTER_JINJA_TEMPLATES_DIRECTORY}/Dockerfile.jinja"                          \
    TFW_STARTER_SUPERVISOR_CONFIG_SOURCE="${TFW_STARTER_JINJA_TEMPLATES_DIRECTORY}/webservice.conf.jinja"              \
    TFW_STARTER_DOCKERFILE_DESTINATION="${TFW_STARTER_WORKING_DIRECTORY}/solvable/Dockerfile"                           \
    TFW_STARTER_SUPERVISOR_CONFIG_DESTINATION="${TFW_STARTER_WORKING_DIRECTORY}/solvable/supervisor/webservice.conf"    \
    TFW_STARTER_WEBSERVICE_DESTINATION="${TFW_STARTER_WORKING_DIRECTORY}/solvable/src/webservice"


RUN pip3 install -r requirements.txt


CMD ["python", "server.py"]