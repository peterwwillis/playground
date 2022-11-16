
APP_NAME := $(shell sh -c 'basename $$(pwd)')
VENV := ../venv-$(APP_NAME)

all: pip format lint

clean: venv-clean py-clean

venv:
	command -v virtualenv || \
        pip3 install virtualenv
	[ -d $(VENV) ] || virtualenv $(VENV)

venv-clean:
	rm -rf $(VENV)

pip: venv
	. $(VENV)/bin/activate ; pip3 install -r requirements.txt

py-clean:
	rm -rf __pycache__

format:
	. $(VENV)/bin/activate ; black *.py

lint:
	. $(VENV)/bin/activate ; flake8 *.py

DOCKER_IMAGE_NAME := $(APP_NAME):latest
docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
