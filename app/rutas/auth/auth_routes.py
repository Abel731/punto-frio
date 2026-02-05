from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from app.conexion.Conexion import Conexion

bp_auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates"
)

@bp_auth.get("/login")
def login():
    return render_template("login.html", error=None)

@bp_auth.post("/login")
def login_post():
    usuario = (request.form.get("usuario") or "").strip()
    password = request.form.get("password") or ""

    con = Conexion().getConexion()
    cur = con.cursor()
    cur.execute("""
        SELECT usuario, password_hash
        FROM usuarios
        WHERE usuario=%s AND activo=TRUE;
    """, (usuario,))
    row = cur.fetchone()
    cur.close(); con.close()

    if not row or not check_password_hash(row[1], password):
        return render_template("login.html", error="Usuario o contraseña incorrectos")

    session["usuario"] = row[0]
    return redirect(request.args.get("next") or url_for("ventas.vista_ventas"))

@bp_auth.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
