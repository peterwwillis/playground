#!/usr/bin/env sh
set -eux

authns-db drop_table user || true
