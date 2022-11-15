#!/usr/bin/env sh
ls -la
pwd
ls -la s3_api
exec ./venv/bin/python s3_api "$@"
