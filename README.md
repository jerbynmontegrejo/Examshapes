# Examshapes

Create Conda Virtual Environment

$ conda create -n "envname" python==3.9.0

Activate Envinronment

$ conda activate envname

##################

Install Packages

$ pip install -r requirements.txt

#################

Migrate and Run the API server

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver

#################

API Routes

Admin Site = http://localhost:8000/admin
Default API Root = http://localhost:8000/api
Register = http://localhost:8000/register
Login = http://localhost:8000/api/login
Account = http://localhost:8000/api/account
Shapes = http://localhost:8000/api/shapes


