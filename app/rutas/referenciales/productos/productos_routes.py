from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.seguridad.auth import login_requerido
from app.rutas.referenciales.productos.productos_api import (
    listar_productos,
    crear_producto,
    actualizar_producto,
    eliminar_producto,
    obtener_producto
)

bp_productos = Blueprint(
    "productos",
    __name__,
    url_prefix="/productos",
    template_folder="templates"
)

@bp_productos.get("/")
@login_requerido
def vista_productos():
    return render_template("productos.html")

# --- API para DataTables ---
@bp_productos.get("/api")
def api_listar():
    # DataTables espera { data: [...] }
    return jsonify({"data": listar_productos()})

@bp_productos.get("/api/<int:producto_id>")
def api_obtener(producto_id):
    p = obtener_producto(producto_id)
    if not p:
        return jsonify({"success": False, "error": "Producto no encontrado"}), 404
    return jsonify({"success": True, "data": p})

@bp_productos.post("/api")
def api_crear():
    try:
        data = request.get_json(force=True)
        return jsonify(crear_producto(data))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@bp_productos.put("/api/<int:producto_id>")
def api_actualizar(producto_id):
    try:
        data = request.get_json(force=True)
        return jsonify(actualizar_producto(producto_id, data))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@bp_productos.delete("/api/<int:producto_id>")
def api_eliminar(producto_id):
    try:
        return jsonify(eliminar_producto(producto_id))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
