export PROJECT_NAME=app

python manage.py migrate
python manage.py makemigrations $PROJECT_NAME 2> /dev/null
python manage.py migrate $PROJECT_NAME 2> /dev/null
echo "Check logs for details."
