#!/usr/bin/env sh
set -eux
CURLHOST="${CURLHOST:-127.0.0.1}"
CURLPORT="${CURLPORT:-7654}"

# Submit request data with URL-query formatting
curl \
    -vvv \
    --get \
    -d "key=foobar" \
    http://$CURLHOST:$CURLPORT/

# Submit multipart/form-data with method GET
curl \
    -vvv \
    -X GET \
    -F "key=foobar" \
    http://$CURLHOST:$CURLPORT/

