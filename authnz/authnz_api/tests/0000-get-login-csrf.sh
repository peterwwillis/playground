#!/usr/bin/env sh
set -eux
AUTHNZ_API_HOST="${AUTHNZ_API_HOST:-127.0.0.1}"
AUTHNZ_API_PORT="${AUTHNZ_API_PORT:-7652}"

curl -s "http://$AUTHNZ_API_HOST:$AUTHNZ_API_PORT/login" "$@" \
    | grep csrf_token \
    | sed -e 's/^.*<//; s/>.*//' \
    | sed -e 's/ /\n/g' \
    | grep value \
    | cut -d \" -f 2 \
    | head -1
