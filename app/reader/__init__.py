from flask import Blueprint

reader_bp = Blueprint("reader_bp", __name__, static_folder="app.static", template_folder="app.templates")

from . import reader_routes
from . import filters
