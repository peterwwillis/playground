#!/bin/sh
docker-compose -f s3-api-compose.yml up --build --always-recreate-deps --force-recreate --abort-on-container-exit
