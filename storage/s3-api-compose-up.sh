#!/bin/sh
docker compose \
    up \
    --build \
     --always-recreate-deps \
    --force-recreate \
    --abort-on-container-exit
