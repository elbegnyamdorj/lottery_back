#!/bin/sh

set -e
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runscript load_lottery
python manage.py runserver 0.0.0.0:8080
# uwsgi --socket :8080 --master --enable-threads --module mysite.wsgi