
APP_NAME := $(shell sh -c 'basename $$(pwd)')

.PHONY: shellcheck tests docker-build clean db-clean

all: shellcheck tests docker-build

clean: db-clean

shellcheck:
	shellcheck $(APP_NAME)

tests:
	make -C tests

db-clean:
	rm -f authnz.db

DOCKER_IMAGE_NAME := $(APP_NAME):latest
docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
