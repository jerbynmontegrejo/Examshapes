# Examshapes

Create Conda Virtual Environment

$ conda create -n "envname" python==3.9.0

Activate Envinronment

$ conda activate envname

##################
Install Postgres/Postgreql and Create Database

Check if you Ubuntu OS packages are up to date
$ sudo apt-get update
then Install postgres/postgresql by this command
$ sudo apt-get install postgresql postgresql-contrib

press 'y' or type 'yes' if anything prompts to proceed with installation

after successful installation verify postgres/postgresql

$ sudo systemctl status postgresql 

Connect to postgres by following this command

$ sudo su -postgres
$ psql

if you're successfully connected to postgres the 'username@computer' must be replaced with 'postgres=#'

you can also run this command instead above

$ sudo -u postgres psql

if you want to quit postgres just type 'exit' on postgres

Change default username 'postgres' with this command

$ ALTER USER postgres RENAME TO 'new_username';

Change password of user by this command

$ ALTER USER 'username' WITH PASSWORD 'password';

or you can create a new user with a new role and you can add priveleges attribute to it

$ CREATE ROLE 'username' WITH SUPERUSER PASSWORD 'password'

Create postgres Database by following this command

$ CREATE DATABASE db_name;

###############

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
Register = http://localhost:8000/api/register
Login = http://localhost:8000/api/login
Account = http://localhost:8000/api/account
Shapes = http://localhost:8000/api/shapes


