#!/bin/bash
pip install -r requirements.txt
(python3 -m gunicorn main.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) & nginx -g "daemon off;"