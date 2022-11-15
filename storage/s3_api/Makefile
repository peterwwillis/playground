
DOCKER_IMAGE_NAME := s3-api:latest

all: venv

clean: venv-clean

venv:
	command -v virtualenv || \
        pip3 install virtualenv
	[ -d venv ] || virtualenv venv

venv-clean:
	rm -rf venv

pip:
	. ./venv/bin/activate ; pip3 install -r requirements.txt

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
