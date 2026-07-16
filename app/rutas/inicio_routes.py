from flask import Blueprint, redirect, url_for

bp_inicio = Blueprint("inicio", __name__)

@bp_inicio.get("/")
def landing_page():
    return redirect(url_for("index.html"))
