# Icky Project

## Prepare and run Backend
```
python3 -m venv [path_to_folder]
source [path_to_folder]/bin/activate
pip install django djangorestframework django-cors-headers
cd icky-project
python manage.py startapp icky-project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Prepare and run frontend
```
cd [path_to_folder]/icky-frontend
npm install
npm run serve
```