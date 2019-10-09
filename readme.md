# Project setup guide

1. Install python (latest version recommended) and pip (latest version recommended)
2. Install postgresql 
3. Install mongodb
4. Create user and database in postgresql (Config to be added in project settings file)
5. Start mongo server
6. Create user in Mongodb.
7. Create admin user inside admin DB
  >> use admin
  >> db.createUser({ user: <username>, pwd: <password>, roles: ["userAdminAnyDatabase"] })
8. Create DB in MongoDB.
  >> use orgstackdb
9. Create user inside orgstackdb DB
  >> db.createUser({	user: <username>,pwd: <password>,roles:[{role: "userAdminAnyDatabase" , db:<database>}]})
10. Install virtualenv
11. Create new virtualenv and activate
12. Go to project folder: __cd orgstack_backend__
13. Install the requirements: __pip install -r requirements.txt__
14. Create the intial migrations: From the root directory,  run __./manage.py makemigrations__ (or python manage.py makemigrations)
15. Migrate the intial migrations __./manage.py migrate__ (or python manage.py migrate)
16. To create the superuser for your django admin panel, run command ./manage.py createsuperuser (or python manage.py createsuperuser)
17. To start the project, run command __./manage.py runserver__ (or python manage.py runserver). By default the server will be running at 127.0.0.1:8000
