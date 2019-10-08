# Project setup guide

1. Install python (latest version recommended) and pip (latest version recommended)
2. Install postgresql 
3. Install mongodb
4. Install virtualenv
5. Create new virtualenv and activate
6. Clone the project and move it inside the virtualenv
7. Inside the project directory, run command cd orgstack_backend
7. Run command pip install -r requirements.txt
8. Now you have all the required packages installed
9. From the root directory of the project,  run command ./manage.py makemigrations (or python manage.py makemigrations)
10. Run command ./manage.py migrate (or python manage.py migrate)
11. To create the superuser for your django admin panel, run command ./manage.py createsuperuser (or python manage.py createsuperuser)
12. To start the project, run command ./manage.py runserver (or python manage.py runserver)