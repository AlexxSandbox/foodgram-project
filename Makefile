.PHONY: run

default: run

define set-default-container
	ifndef c
	c = web
	else ifeq (${c},all)
	override c=
	endif
endef

define use-env
	include .env
#	export
endef


set-container:
	$(eval $(call set-default-container))

build: set-container
	docker-compose build ${c}

run:
	docker-compose up -d --force-recreate ${c}

dev:
	docker-compose -f docker-compose.yaml up -d --force-recreate ${c}

restart: set-container
	docker-compose restart ${c}

stop: set-container
	docker-compose stop ${c}

down:
	docker-compose down

exec: set-container
	docker-compose exec ${c} /bin/bash

log: set-container
	docker-compose logs -f ${c}

makemigrations:
	docker-compose exec web python manage.py makemigrations

migrate: makemigrations
	docker-compose exec web python manage.py migrate

collectstatic:
	docker-compose exec web ./manage.py collectstatic --noinput
	docker-compose exec web ./manage.py clear_templates_cache
