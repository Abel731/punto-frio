from flask import redirect, url_for
from app import crear_app

app = crear_app()

@app.get("/")
def inicio():
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
