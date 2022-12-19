
##############################################
FROM python:3.10.8-alpine3.16 AS base-deps

# Work around traffic-inspection proxies
COPY bundle.pem /etc/ssl/certs/ca-bundle.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-bundle.crt
ARG HTTP_PROXY
ENV HTTP_PROXY=$HTTP_PROXY
ENV HTTPS_PROXY=$HTTP_PROXY
ENV http_proxy=$HTTP_PROXY
ARG NO_PROXY
ENV NO_PROXY=$NO_PROXY
ENV no_proxy=$NO_PROXY

ARG APP_NAME
ENV APP_NAME=$APP_NAME

RUN [ -n "${APP_NAME:-}" ] || { echo "ERROR: You must pass APP_NAME as a build arg to this Docker container" ; exit 1 ; }

WORKDIR /app/${APP_NAME}

COPY requirements.txt Makefile /app/${APP_NAME}/

#RUN apk add --allow-untrusted --repository http://dl-cdn.alpinelinux.org/alpine/v3.16/main \

RUN env | sort ; apk add \
        curl make sqlite \
    && make venv pip

# Add authnz-db to the path
ENV PATH=/app/${APP_NAME}/authnz-db:$PATH

##############################################
FROM base-deps AS production

COPY . /app/${APP_NAME}
