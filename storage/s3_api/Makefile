
DOCKER_IMAGE_NAME := s3-api:latest

.PHONY: tests

all: venv

clean: venv-clean py-clean

tests:
	make -C tests

venv:
	command -v virtualenv || \
        pip3 install virtualenv
	[ -d venv ] || virtualenv venv

venv-clean:
	rm -rf venv

pip:
	. ./venv/bin/activate ; pip3 install -r requirements.txt

py-clean:
	rm -rf __pycache__

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
