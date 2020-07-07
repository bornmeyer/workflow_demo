#!/bin/bash
python -m pip install --user --upgrade pip
python -m pip install --user virtualenv
python -m venv env
source env/bin/activate
echo which python
read -p "Press any key to continue... " -n1 -s
pip install -r requirements.txt

python manage.py migrate
python manage.py test app.tests
python manage.py runserver