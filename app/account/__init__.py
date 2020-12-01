from flask import Blueprint

account_bp = Blueprint("account_bp", __name__, static_folder="static", static_url_path="/account_bp/static/",
                       template_folder="templates")

from . import account_routes
