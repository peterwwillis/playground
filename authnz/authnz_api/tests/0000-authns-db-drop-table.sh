#!/usr/bin/env sh
set -eux

authnz-db drop_table user || true
