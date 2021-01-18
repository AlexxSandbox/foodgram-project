# "FOODgram" - food assistant

![CI Status](https://github.com/AlexxSandbox/foodgram-project/workflows/FOODgram%20workflow/badge.svg)
![Top language](https://img.shields.io/github/languages/top/AlexxSandbox/foodgram-project)
![GitHub last commit](https://img.shields.io/github/last-commit/AlexxSandbox/foodgram-project)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/alexxdockerhub/foodgram)

An online service where users can publish recipes, subscribe to publications of other users, add recipes they like to the Favorites list, and download a summary list of products needed to prepare one or more selected dishes before going to the store.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them

* [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Install Docker-compose](https://docs.docker.com/compose/install/)

### How it work
Create .env file:
```
$ touch .env
```
Edit .env with nano or VIM:
```
$ DB_ENGINE=django.db.backends.postgresql
$ DB_NAME=*\<YOURDB>\*
$ POSTGRES_USER=*\<YOURNAME>\*
$ POSTGRES_PASSWORD=*\<YOURPASSWORD>\*
$ DB_HOST=db
$ DB_PORT=5432
$ EMAIL_HOST=*\<YOURHOST>\*
$ EMAIL_USER=*\<YOURNAME>\*
$ EMAIL_PASSWORD=*\<YOURPASSWORD>\*
```
Build the new image and spin up the containers:
```
$ sudo docker-compose up -d --build
```
Create superuser for Django admin:
```
$ docker container exec -it APIDOCKER bash
$ python manage.py createsuperuser
$ ...
```
Ready!
Run browser and Bon Appetit. [Push this link](http://84.201.172.218/).

*To stop and remove containers, networks run:
```
$ sudo docker-compose down
```

## Built With
* [Django](https://docs.djangoproject.com/en/3.1/) - Web framework on Pythongtht
* [PostgreSQL](https://hub.docker.com/_/postgres) - The open source object-relation database
* [Gunicorn](https://gunicorn.org/) - Puthon WSGI HTTP Server  for Unix
* [nginx](https://hub.docker.com/_/nginx) - Nginx (pronounced "engine-x") is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).
* [alexxdockerhub/foodgram](https://hub.docker.com/r/alexxdockerhub/foodgram-project) - Food assistant by Django.
* [Python, CSS, HTML and JS]()

## Contributing
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
Please note we have a code of conduct, please follow it in all your interactions with the project.

## Versioning
Latest versions available, see the [GitHub](https://github.com/AlexxSandbox/foodgram-project) or [DockerHub](https://hub.docker.com/r/alexxdockerhub/foodgram-project). 

## Authors
**Aleksandr Sergeev** - [GitHub](https://github.com/AlexxSandbox/)

## License
This project is licensed under the BSD 3-Clause License

## Acknowledgments
* Docs, searching in google and my patience.