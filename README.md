docker build .
docker-compose build
docker-compose run app sh -c "django-admin.py startproject app ."
https://travis-ci.org/
sudo docker-compose run app sh -c "python manage.py test"
sudo docker-compose run app sh -c "python manage.py startapp core"
sudo docker-compose run app sh -c "python manage.py makemigrations core"