#!/usr/bin/env sh
set -eux

docker-compose \
    up \
    --build \
    --always-recreate-deps \
    --force-recreate \
    --abort-on-container-exit \
    "$@"
