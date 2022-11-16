#!/usr/bin/env sh
set -eu
[ "${DEBUG:-0}" = "1" ] && set -x

OSTYPE="${OSTYPE:-linux}" # this is unset in busybox containers

ls -la ..
pwd

dir="${MODULE_DIR:-$(cd $(dirname "$0") && pwd -P)}"
cd "$dir" # change to the source directory

APP_NAME="${APP_NAME:-$(basename "$(pwd)")}"
venv="${VENV_DIR:-$(cd "../venv-${APP_NAME}" && pwd -P)}"
. "$venv/bin/activate" # activate the venv in parent directory

head -1 "$venv/bin/gunicorn" # double check this hard-coded the correct venv path

#    --access-logfile \

exec "$venv/bin/gunicorn" \
    --workers=3 \
    -b "$LISTEN_ADDRESS:$LISTEN_PORT" \
    --reload \
    --preload \
    "wsgi" \
    "$@"

