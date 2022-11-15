#!/usr/bin/env python3

import io
import os
import sys
import json

from minio import Minio
from minio.error import S3Error

from flask import Flask, Response, stream_with_context, request, jsonify
app = Flask(__name__)

import urllib3
from datetime import timedelta

class Storage_Backend_S3(object):
    client = None
    def __init__(self):
        self.connect()
    def connect(self):
        self.client = Minio(
            os.environ['S3_ENDPOINT'],
            access_key=os.environ['S3_ACCESS_KEY'],
            secret_key=os.environ['S3_SECRET_KEY'],
            secure=True,
        )
    def get_object(self, key):
        response = self.client.get_object( os.environ['S3_BUCKET'], key )
        return response

    def put_object(self, key, content):
        found = self.client.bucket_exists(os.environ['S3_BUCKET'])
        if not found:
            self.client.make_bucket(os.environ['S3_BUCKET'])
        else:
            print("Bucket '%s' already exists" % os.environ['S3_BUCKET'])
        raw_content = io.BytesIO(content)
        raw_content_size = raw_content.getbuffer().nbytes
        return self.client.put_object( os.environ['S3_BUCKET'], key, raw_content, raw_content_size )

@app.route("/", methods=['GET'])
def Storage_Backend_S3_Get():
    key = flask_get_arg('key')
    s3 = Storage_Backend_S3()

    try:
        data = s3.get_object(key)
        def generate():
            for d in data.stream(32*1024):
                yield d
        return Response(generate(), mimetype='application/octet-stream')
    except S3Error as exc:
        jsonresp = jsonify( { 'status': 'failed', 'error': "Failed to query storage for key '%s': %s" % (key, exc) } )
        return Response(response=jsonresp, mimetype='application/json')

@app.route('/', methods=['PUT'])
def Storage_Backend_S3_Put():
    key = flask_get_arg('key')
    content = flask_get_content('content')
    s3 = Storage_Backend_S3()

    try:
        resp = s3.put_object(key, content)
        return jsonify( { 'status': 'success' } )
    except S3Error as exc:
        return jsonify( { 'status': 'failed', 'error': "Failed to query storage for key '%s': %s" % (key, exc) } )

def flask_get_arg(name):
    if name in request.form:
        #print("got form item '%s'='%s'" % (name,value), file=sys.stderr)
        return request.form[name]
    else:
        #print("got arg item '%s'='%s'" % (name,value), file=sys.stderr)
        return request.args.get(name)

def flask_get_content(name):
    if name in request.files:
        contentf = request.files[name]
        if contentf.filename == '':
            flash('No selected file')
            return redirect(request.url)
        #print("got form content '%s'" % (name))
        return contentf.read()
    else:
        #print("got arg content '%s'" % name)
        return request.args.get(name)


def main():
    debug = False
    if 'DEBUG' in os.environ and os.environ['DEBUG']: debug = True
    app.run(os.environ['FLASK_ADDRESS'], os.environ['FLASK_PORT'], debug )

if __name__ == "__main__":
    main()
