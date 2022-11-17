
APP_NAME := $(shell sh -c 'basename $$(pwd)')

.PHONY: tests docker-build clean db-clean

all: tests docker-build

clean: db-clean

tests:
	make -C tests

db-clean:
	rm -f authnz.db

DOCKER_IMAGE_NAME := $(APP_NAME):latest
docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
