from flask import Blueprint


reader_bp = Blueprint("reader_bp", __name__, static_folder="app.static", template_folder="app.templates")
print(f"Reader __init__: {__name__}")

from . import reader_routes
from . import filters
