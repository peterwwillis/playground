FROM alpine:3.16

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

COPY Makefile /app/

#RUN apk add --allow-untrusted --repository http://dl-cdn.alpinelinux.org/alpine/v3.16/main \

RUN apk add \
        sqlite

COPY authnz-db authnz-db

# Add authnz-db to the path
ENV PATH=/app:$PATH
