#!/usr/bin/env sh
set -eu

for i in `seq 1 4` ; do
    authnz-db user get "test$i"
done
