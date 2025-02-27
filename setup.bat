
@echo off
cd /d D:\SkincareProject

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install django djangorestframework

echo Creating Django project...
if not exist manage.py (
    django-admin startproject skincare_project .
) else (
    echo Django project already exists, skipping creation...
)

echo Creating Django app...
if not exist skincare_app (
    django-admin startapp skincare_app
) else (
    echo Django app 'skincare_app' already exists, skipping creation...
)

echo Running migrations...
if exist manage.py (
    python manage.py migrate
) else (
    echo Error: manage.py not found in D:\SkincareProject
    exit /b 1
)

echo Creating superuser...
set DJANGO_SUPERUSER_USERNAME=skincare_admin
set DJANGO_SUPERUSER_EMAIL=admin@skincare.com
set DJANGO_SUPERUSER_PASSWORD=skincare_pass123
python manage.py createsuperuser --noinput


echo Starting Django server...
python manage.py runserver
