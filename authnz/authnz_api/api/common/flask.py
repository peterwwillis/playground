
from flask import flash, redirect, request

def flask_get_arg(name):
    if name in request.form:
        # print("got form item '%s'='%s'" % (name,value), file=sys.stderr)
        return request.form[name]
    else:
        # print("got arg item '%s'='%s'" % (name,value), file=sys.stderr)
        return request.args.get(name)


def flask_get_content(name):
    if name in request.files:
        contentf = request.files[name]
        if contentf.filename == "":
            flash("No selected file")
            return redirect(request.url)
        # print("got form content '%s'" % (name))
        return contentf.read()
    else:
        # print("got arg content '%s'" % name)
        return request.args.get(name)

