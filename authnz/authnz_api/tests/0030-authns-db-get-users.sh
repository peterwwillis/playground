#!/usr/bin/env sh
set -eu

for i in `seq 1 4` ; do
    authns-db user get "test$i"
done
