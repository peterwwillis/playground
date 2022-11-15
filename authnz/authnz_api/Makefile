
DOCKER_IMAGE_NAME := authnz-api:latest

all: pip format lint

clean: venv-clean py-clean

venv:
	command -v virtualenv || \
        pip3 install virtualenv
	[ -d venv ] || virtualenv venv

venv-clean:
	rm -rf venv

pip: venv
	. ./venv/bin/activate ; pip3 install -r requirements.txt

py-clean:
	rm -rf __pycache__

format:
	. ./venv/bin/activate ; black *.py

lint:
	. ./venv/bin/activate ; flake8 *.py

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
