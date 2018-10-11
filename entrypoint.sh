#!/bin/bash
python3 manage.py collectstatic --noinput && python3 manage.py migrate
uwsgi --plugins=python3 --chdir=/var/www --socket=0.0.0.0:9000 --module=lernino.wsgi:application --processes=4 --protocol=http --static-map /media=/var/www/media --static-map /static=/var/www/staticfiles
