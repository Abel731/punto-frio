from flask import Blueprint, render_template, jsonify, request
from app.seguridad.auth import login_requerido
from app.rutas.operaciones.ventas.ventas_api import (
    listar_productos_para_venta,
    crear_venta,
    ventas_del_dia,
    total_del_dia,
    resumen_hoy
)

bp_ventas = Blueprint(
    "ventas",
    __name__,
    url_prefix="/ventas",
    template_folder="templates"
)

@bp_ventas.get("/")
@login_requerido
def vista_ventas():
    # cargamos productos para el select
    productos = listar_productos_para_venta()
    return render_template("ventas.html", productos=productos)

@bp_ventas.get("/api")
def api_listar_ventas_dia():
    return jsonify({"data": ventas_del_dia(), **total_del_dia(), "resumen": resumen_hoy()})

@bp_ventas.post("/api")
def api_crear_venta():
    try:
        data = request.get_json(force=True)
        return jsonify(crear_venta(data))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
