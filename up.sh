#!/bin/bash

if [ "$VIRTUAL_ENV" == "" ]; then
    echo "ERROR: you must be in a virtual environment to run this script"
    exit 1
else
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver 127.0.0.1:8011
fi