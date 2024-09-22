#!/bin/bash
set -e

echo "Updating system..."
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
sudo apt install -y nginx
sudo apt install -y virtualenv

echo "Setting up virtual environment..."
virtualenv "~/.venv"
source "~/.venv/bin/activate"
pip install -r "~/${APP_NAME}/requirements.txt"

echo "Configuring gunicorn..."
sudo cp "~/${APP_NAME}/gunicorn/gunicorn.socket" "/etc/systemd/system/gunicorn.socket"
sudo cp "~/${APP_NAME}/gunicorn/gunicorn.service" "/etc/systemd/system/gunicorn.service"
sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service

echo "Configuring nginx..."
sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default
sudo cp "~/${APP_NAME}/nginx/nginx.conf" "/etc/nginx/sites-available/project"
sudo ln -s "/etc/nginx/sites-available/project" "/etc/nginx/sites-enabled/"
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx

echo "Running collectstatic command..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py migrate

echo "Restarting Gunicorn and Nginx services..."
sudo service gunicorn restart
sudo service nginx restart
