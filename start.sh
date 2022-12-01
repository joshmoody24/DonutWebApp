#!/bin/bash
python manage.py migrate
python manage.py loaddata ./MainApp/datadump/seed.json
python manage.py runserver 0.0.0.0:8000