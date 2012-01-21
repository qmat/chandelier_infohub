#!/bin/bash
set -e

LOGFILE=/var/log/supervisor/twobbler/gunicorn.log
NUM_WORKERS=3
ADDRESS=127.0.0.1:3000
USER=mat
GROUP=mat

cd /home/$USER/src/chandelier_infohub/
source /home/$USER/.virtualenvs/chandelier_infohub/bin/activate
exec /home/$USER/.virtualenvs/chandelier_infohub/bin/gunicorn_django -w $NUM_WORKERS \
    --user=$USER --group=$GROUP --bind $ADDRESS
