from flask import Blueprint

BP_NAME = 'routes'
bp = Blueprint(BP_NAME, __name__)

from . import home, login, logout
