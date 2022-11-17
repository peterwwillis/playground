#!/usr/bin/env sh
set -eu

for i in `seq 1 4` ; do
    authnz-db user auth "test$i" "password$i"
    if authnz-db user auth test1 wrongpassword ; then
        echo "$0: Error: auth password did not fail as expected" ; exit 1
    fi
done
