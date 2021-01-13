# "FOODgram" - food assistant

![CI Status](https://github.com/AlexxSandbox/foodgram-project/workflows/YaMDB%20api%20workflow/badge.svg)
![Top language](https://img.shields.io/github/languages/top/AlexxSandbox/foodgram-project)
![GitHub last commit](https://img.shields.io/github/last-commit/AlexxSandbox/foodgram-project)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/alexxdockerhub/foodgram-project)

An online service where users can publish recipes, subscribe to publications of other users, add recipes they like to the Favorites list, and download a summary list of products needed to prepare one or more selected dishes before going to the store.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Install Docker-compose](https://docs.docker.com/compose/install/)

### How it work
Generate .env file:
* auto
```
$ sudo ./bin/create_enfile.sh
```
* manual
```
$ touch .env

$ DB_ENGINE=django.db.backends.postgresql
$ DB_NAME=*\<YOURDB>\*
$ POSTGRES_USER=*\<YOURNAME>\*
$ POSTGRES_PASSWORD=*\<YOURPASSWORD>\*
$ DB_HOST=db
$ DB_PORT=5432
```
Build the new image and spin up the containers:
```
$ sudo docker-compose up -d --build
```
or
```
$ make dev
```
Create migrations:
```
$ make makemigrations
```
```
$ make migrate
```
Create superuser for Django admin:
```
$ make exec
$ python manage.py createsuperuser
$ ...
```
Ready!
Run browser and get Token [localhost/api/v1/auth/token](https://localhost:8000/api/v1/auth/token/)

*To stop and remove containers, networks run:
```
$ make down
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.1/) - Web framework on Pythongtht
* [Django REST](https://www.django-rest-framework.org/) - The REST framework
* [drfpasswordless](https://pypi.org/project/drfpasswordless/) - Passwordless auth for Django Rest Framework Token Authentication
* [PostgreSQL](https://hub.docker.com/_/postgres) - The open source object-relation database
* [Gunicorn](https://gunicorn.org/) - Puthon WSGI HTTP Server  for Unix
* [nginx](https://hub.docker.com/_/nginx) - Nginx (pronounced "engine-x") is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).
* [yamdb_api](https://hub.docker.com/r/alexxdockerhub/yamdb) - API service for movie reviews.

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
Please note we have a code of conduct, please follow it in all your interactions with the project.

#### Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you

## Versioning

Latest versions available, see the [GitHub](https://github.com/AlexxSandbox/foodgram-project). 

## Authors

* **Aleksandr Sergeev** - [AlexxSandbox](https://github.com/AlexxSandbox/)

## License

This project is licensed under the BSD 3-Clause License

## Acknowledgments

* Friends, searching in google and docs.