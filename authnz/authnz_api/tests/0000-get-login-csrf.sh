#!/usr/bin/env sh
set -eu
[ "${DEBUG:-0}" = "1" ] && set -x && CURLVERBOSE="-vvv"

AUTHNZ_API_HOST="${AUTHNZ_API_HOST:-127.0.0.1}"
AUTHNZ_API_PORT="${AUTHNZ_API_PORT:-7652}"

curl ${CURLVERBOSE:-} \
    -c "/tmp/cookies.txt" \
    -b "/tmp/cookies.txt" \
    "http://$AUTHNZ_API_HOST:$AUTHNZ_API_PORT/login" \
    "$@" \
    | grep csrf_token \
    | sed -e 's/^.*<//; s/>.*//' \
    | sed -e 's/ /\n/g' \
    | grep value \
    | cut -d \" -f 2 \
    | head -1

echo "Cookies:" 1>&2
cat /tmp/cookies.txt 1>&2
