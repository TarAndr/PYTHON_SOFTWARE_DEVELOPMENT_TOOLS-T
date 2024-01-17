python -m pip install Django
python import django
python print(django.get_version())
django-admin startproject mysite
cd mysite
python manage.py startapp myapp
python manage.py makemigrations
python manage.py migrate