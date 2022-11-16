#!/usr/bin/env sh
set -eux

if [ "${1:-}" = "--no-cache" ] ; then
    shift
    docker compose build --no-cache --progress=plain "$@"
fi

docker compose \
    up \
    --build \
    --always-recreate-deps \
    --force-recreate \
    --abort-on-container-exit \
    "$@"
