#!/usr/bin/env sh
set -eux

for i in `seq 1 4` ; do
    authns-db user create -u "test$i" -n "Test User $i" -e "test$i@example.com" -p "password$i"
done
