
APP_NAME := $(shell sh -c 'basename $$(pwd)')
VENV := ../venv-$(APP_NAME)

.PHONY: bundle docker-build tests

all: bundle pip format lint

clean: venv-clean py-clean

tests:
	make -C tests

venv:
	if ! command -v virtualenv ; then \
        pip3 install virtualenv ; \
	fi
	[ -d $(VENV) ] || virtualenv $(VENV)

venv-clean:
	rm -rf $(VENV)

pip: venv
	. $(VENV)/bin/activate ; pip3 install -r requirements.txt

py-clean:
	rm -rf __pycache__

format:
	. $(VENV)/bin/activate ; black

lint:
	. $(VENV)/bin/activate ; flake8

DOCKER_IMAGE_NAME := $(APP_NAME):latest
docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .

bundle:
	if [ ! -e bundle.pem ] ; then \
		if [ -e /etc/ssl/cert.pem ] ; then \
			cp /etc/ssl/cert.pem bundle.pem ; \
		fi ; \
	fi
