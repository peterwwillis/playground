#!/usr/bin/env sh
set -eux
CURLHOST="${CURLHOST:-127.0.0.1}"
CURLPORT="${CURLPORT:-7654}"

tmpfile=""
_cleanup () {
    [ -n "${tmpfile:-}" ] && rm -f "$tmpfile"
}
trap _cleanup EXIT

tmpfile="$(mktemp)"
printf "%s\n" "This is a muti-line file.

It is a test of the PUT operation.

Today's date is $(date)." > "$tmpfile"

# Submit multipart/form-data request using method PUT
curl \
    -vvv \
    -X PUT \
    -F "key=foobar" \
    -F "content=@$tmpfile" \
    http://$CURLHOST:$CURLPORT/

