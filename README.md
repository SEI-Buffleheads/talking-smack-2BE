# TALKIN SHMACK API

Welcome to the talkin shmack API! Why have a conversation, when you could just Schmack em? 👋
This API was made using Django and Python with a Postgres database.

**_Base API Link: https://talking-smack-2be-production.up.railway.app/_**

Deployed Frontend: ***https://deploy-preview-53--genuine-marshmallow-56fd7d.netlify.app/***

Frontend Repo: **_ https://github.com/SEI-Buffleheads/talkin-smack-fe _**

Features...

user authentication and authorization implemented using the Knox package(https://james1345.github.io/django-rest-knox/) for generating user tokens, tokens are stored in the users cookies until a user has logged out or has been cleared by the user.

endpoints for...

- signing up.
- logging in.
- create read, update and delete a user.
- verifying a user.
- create, read, update and delete a smhack post.
- create, read, update and delete reply's made on a shmack post.

**_To view the full talkin-shmach api documentation please visit the link below:_**

### https://documenter.getpostman.com/view/23919886/2s8YszPq5D

# Getting started locally

- mkvirtualenv <directory name>
- pip install -r requirements.txt
- pip freeze (Check if dependencies installed)
- psql postgres -f create-database.sql
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py createsuperuser
- python3 manage.py runserver

# Some packages installed...

```
Django==4.1.3
django-cors-headers==3.13.0
django-rest-knox==4.2.0
djangorestframework==3.14.0
gunicorn==20.1.0
pipenv==2022.11.11
psycopg2-binary==2.9.5
pycparser==2.21
python-dotenv==0.21.0
sqlparse==0.4.3
virtualenv==20.16.7
virtualenvwrapper==4.8.4
whitenoise==6.2.0
```

# Problems Faced During development...

- understanding all the type of relationships that models can have with other models.
- user authorization
- Implementing user, connnecting Django built in user to custom user. Due to a custom user, resources to find solutions were limited.
- timeline
- getting started locally.
- merge conflicts
