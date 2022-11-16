#!/usr/bin/env sh
set -eux

authnz-db load_schema ../schema-sqlite3.sql
