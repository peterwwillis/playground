FROM python:3.10.8-alpine3.16

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

WORKDIR /app/

COPY requirements.txt Makefile /app/

#RUN apk add --allow-untrusted --repository http://dl-cdn.alpinelinux.org/alpine/v3.16/main \

RUN apk add \
        curl make \
    && make venv pip
