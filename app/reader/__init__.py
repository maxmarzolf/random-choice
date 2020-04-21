from flask import Flask, Blueprint


reader_bp = Blueprint("reader_bp", __name__, static_folder="static", template_folder="templates")


from . import reader_routes