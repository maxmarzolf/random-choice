from flask import Flask, Blueprint


creator_bp = Blueprint("creator_bp", __name__, static_folder="static", static_url_path="/creator_bp/static/", template_folder="templates")
print(f"Creator __init__: {__name__}")


from . import creator_routes
