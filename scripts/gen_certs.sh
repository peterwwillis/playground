#!/usr/bin/env bash
set -eux

SAN_NAME="$1"

mkdir -p certs/CAs

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
    -subj "/C=US/ST=GD/L=SZ/O=Acme, Inc./CN=${SAN_NAME}" \
    -out certs/private.csr

printf "subjectAltName=DNS:${SAN_NAME},DNS:${SAN_NAME}.localdomain" > extfile.tmp
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

