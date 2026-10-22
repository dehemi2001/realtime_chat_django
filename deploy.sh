#!/bin/bash
set -e
cd /home/ubuntu/realtime_chat_django
git fetch origin main
git reset --hard origin/main
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
sudo systemctl restart daphne_chat
sudo systemctl reload nginx
