#!/usr/bin/env sh
set -eux

authns-db load_schema ../schema-sqlite3.sql
