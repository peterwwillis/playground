#!/usr/bin/env sh
set -eux
AUTHNZ_API_HOST="${AUTHNZ_API_HOST:-127.0.0.1}"
AUTHNZ_API_PORT="${AUTHNZ_API_PORT:-7652}"

# Add script dir to PATH
dir="$( cd "$(dirname "$0")" && pwd -P)"
export PATH="$dir:$PATH"

token="$(0000-get-login-csrf.sh "$@")"

user_id="test1"
password="password1"

curl -vvv \
    -c "/tmp/cookies.txt" \
    -b "/tmp/cookies.txt" \
    -F "csrf_token=$token" \
    -F "user_id=$user_id" \
    -F "password=$password" \
    "http://$AUTHNZ_API_HOST:$AUTHNZ_API_PORT/login" \
    "$@"

echo "Cookies:"
cat /tmp/cookies.txt
