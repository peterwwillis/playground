#!/usr/bin/env bash
set -eux
mkdir -p certs
config_1="$(openssl version -d | cut -d \" -f 2 | sed -e 's/$/\/openssl.cnf/')"
config_2="$(printf "[SAN]\nsubjectAltName='DNS.1:*.s3,DNS.2:s3,DNS.3:s3.localdomain'")"

#openssl req -x509 \
#            -sha256 -days 356 \
#            -nodes \
#            -newkey rsa:2048 \
#            -subj "/CN=s3/C=US/L=San Fransisco" \
#            -extfile "subjectAltName=DNS:example.com,DNS:www.example.com" \
#            -keyout certs/private.key -out certs/public.crt

openssl genrsa \
    -out certs/CAs/ca.key \
    4096

openssl req \
    -new \
    -x509 \
    -sha256 \
    -days 365 \
    -key certs/CAs/ca.key \
    -subj "/C=US/ST=GD/L=SZ/O=Acme, Inc./CN=Acme Root CA" \
    -out certs/CAs/ca.crt

openssl req \
    -sha256 \
    -newkey rsa:4096 \
    -nodes \
    -keyout certs/private.key \
    -subj "/C=US/ST=GD/L=SZ/O=Acme, Inc./CN=s3" \
    -out certs/private.csr

printf "subjectAltName=DNS:s3,DNS:s3.localdomain" > extfile.tmp
openssl x509 \
    -req \
    -sha256 \
    -extfile ./extfile.tmp \
    -days 365 \
    -in certs/private.csr \
    -CA certs/CAs/ca.crt \
    -CAkey certs/CAs/ca.key \
    -CAcreateserial \
    -out certs/public.crt
rm -f extfile.tmp


cat certs/CAs/ca.crt certs/public.crt > certs/bundle.crt

