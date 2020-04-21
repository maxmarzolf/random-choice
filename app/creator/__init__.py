from flask import Flask, Blueprint


creator_bp = Blueprint("creator_bp", __name__, static_folder="static", template_folder="templates")


from . import creator_routes