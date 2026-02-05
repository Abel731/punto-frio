from functools import wraps
from flask import session, redirect, url_for, request

def login_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("usuario"):
            return redirect(url_for("auth.login", next=request.path))
        return f(*args, **kwargs)
    return wrapper
