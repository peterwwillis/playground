#!/usr/bin/env sh
set -eux

./authnz-db/tests/0000-authnz-db-drop-table.sh
./authnz-db/tests/0010-authnz-db-load-schema.sh
./authnz-db/tests/0020-authnz-db-create-users.sh
