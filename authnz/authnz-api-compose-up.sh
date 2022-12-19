#!/usr/bin/env sh
set -eux

if [ "${1:-}" = "--no-cache" ] ; then
    shift
    docker compose build --no-cache --progress=plain "$@"
fi

#--abort-on-container-exit \

docker compose \
    up \
    --build \
    --always-recreate-deps \
    --force-recreate \
    "$@"
