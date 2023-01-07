#!/bin/sh

set -e
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runscript load_lottery
uwsgi --socket :8080 --master --enable-threads --module mysite.wsgi