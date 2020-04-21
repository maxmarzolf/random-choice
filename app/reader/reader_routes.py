from flask import Flask, render_template, request

from . import reader_bp


@reader_bp.route("/")
def reader_home():
    return "reader home!"


@reader_bp.route("/post/<int:post_id>")
def read_post(post_id):
    return "read a post!"