# DjangoSocialNetwork
Social network on Pyhon/Django 
==============================

local launch
------------

* `git clone https://github.com/DolphinHMPY/DjangoSocialNetwork.git`
* `cd DjangoSocialNetwork`
* add `env`
    * `python3 -m venv env`
    * `source env/bin/activate`
    * `pip install -r requirements.txt`
* `python ./social_network/manage.py migrate`
* `python ./social_network/manage.py runserver 8080`
* `python ./web_app/manage.py runserver 8000`

docker
------

* `docker build -t python-django -f Dockerfile .`
* `docker-compose up`
* `docker exec -it djangosocialnetwork_rest_api_1 /bin/sh -с  'python manage.py migrate'` 
<!-- TODO: ADD WEB_APP TO DOCKER-COMPOSE -->
* add `env`
    * `python3 -m venv env`
    * `source env/bin/activate`
    * `pip install -r requirements.txt`
* `python ./web_app/manage.py runserver 8000`