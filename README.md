#Start file

- mkvirtualenv <directory name>
- pip install -r requirements.txt
- pip freeze (Check if dependencies installed)
- psql postgres -f create-database.sql
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py createsuperuser
- python3 manage.py runserver
