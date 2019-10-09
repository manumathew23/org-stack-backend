# Project setup guide

1. Install python (latest version recommended) and pip (latest version recommended)
2. Install postgresql 
3. Install mongodb
4. Install virtualenv
5. Create new virtualenv and activate
6. Go to project folder: __cd orgstack_backend__
7. Install the requirements: __pip install -r requirements.txt__
8. Create the intial migrations: From the root directory,  run __./manage.py makemigrations__ (or python manage.py makemigrations)
9. Migrate the intial migrations __./manage.py migrate__ (or python manage.py migrate)
10. To create the superuser for your django admin panel, run command ./manage.py createsuperuser (or python manage.py createsuperuser)
11. To start the project, run command __./manage.py runserver__ (or python manage.py runserver). By default the server will be running at 127.0.0.1:8000
