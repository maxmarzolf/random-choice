from flask import Flask, Blueprint


reader_bp = Blueprint("reader_bp", __name__, static_folder="static", static_url_path="/reader_bp/static/", template_folder="templates")


from . import reader_routes

from . import filters