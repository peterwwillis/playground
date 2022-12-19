#!/usr/bin/env sh
set -eu
[ "${DEBUG:-0}" = "1" ] && set -x

cpu_cores="$(cat /proc/cpuinfo | grep processor | wc -l)"
WORKERS_NUM="${WORKERS_NUM:-$((cpu_cores * 2))}"
THREADS_NUM="${THREADS_NUM:-$((cpu_cores * 4))}"

OSTYPE="${OSTYPE:-linux}" # this is unset in busybox containers

dir="${MODULE_DIR:-$(cd $(dirname "$0") && pwd -P)}"
cd "$dir" # change to the source directory

APP_NAME="${APP_NAME:-$(basename "$(pwd)")}"
venv="${VENV_DIR:-$(cd "../venv-${APP_NAME}" && pwd -P)}"
. "$venv/bin/activate" # activate the venv in parent directory

#    --preload \

set -x
exec "$venv/bin/gunicorn" \
    --workers="$WORKERS_NUM" \
    -b "$LISTEN_ADDRESS:$LISTEN_PORT" \
    --reload \
    --reload-engine=inotify \
    --threads="$THREADS_NUM" \
    --access-logfile=- \
    "app:run()" \
    "$@"
