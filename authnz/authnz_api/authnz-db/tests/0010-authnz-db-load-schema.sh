#!/usr/bin/env sh
set -eux

SCHEMA_FILE="${SCHEMA_FILE:-../schema-sqlite3.sql}"

authnz-db load_schema "$SCHEMA_FILE"
