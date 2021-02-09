
find . -path "*/migrations/*.pyc"  -delete
find . -path */migrations/*.py -not -name __init__.py -delete
rm db.sqlite3
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
