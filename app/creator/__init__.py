from flask import Blueprint

creator_bp = Blueprint("creator_bp", __name__, static_folder="static", static_url_path="/creator_bp/static/",
                       template_folder="templates")

from . import creator_routes
