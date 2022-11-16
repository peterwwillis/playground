from flask import Blueprint, render_template

from . import bp

@bp.route('/')
@bp.route('/home')
def AuthNZ_Home():
    return render_template("index.html")
    # if current_user.is_authenticated:
    # else:
    #    return '<a class="button" href="/login">Login</a>'

