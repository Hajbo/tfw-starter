#!/bin/sh
# this script is used to boot the Docker container

exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - startr:app