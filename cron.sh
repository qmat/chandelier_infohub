#!/bin/bash
set -e

cd /Users/mat/src/chandelier_infohub/
source /Users/mat/.virtualenvs/chandelier_infohub/bin/activate
exec /Users/mat/.virtualenvs/chandelier_infohub/bin/python manage.py cron
