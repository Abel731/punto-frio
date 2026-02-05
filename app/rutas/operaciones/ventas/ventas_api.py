from app.dao.operaciones.ventas.ventas_dao import VentaDAO
from app.dao.referenciales.productos.producto_dao import ProductoDAO

venta_dao = VentaDAO()
prod_dao = ProductoDAO()

def listar_productos_para_venta():
    datos = prod_dao.listar_para_venta()
    return [{"id": p[0], "nombre": p[1], "precio_venta": p[2], "stock": p[3]} for p in datos]

def crear_venta(data: dict):
    producto_id = int(data.get("producto_id"))
    cantidad = int(data.get("cantidad"))
    metodo_pago = data.get("metodo_pago", "efectivo")

    venta_id = venta_dao.crear_venta_simple(producto_id, cantidad, metodo_pago)
    return {"success": True, "venta_id": venta_id}

def ventas_del_dia():
    datos = venta_dao.ventas_del_dia()
    # id, fecha, total, nombre, cantidad, precio_unitario, subtotal
    return [{
        "venta_id": r[0],
        "fecha": r[1].strftime("%Y-%m-%d %H:%M:%S"),
        "total": r[2],
        "producto": r[3],
        "cantidad": r[4],
        "precio_unitario": r[5],
        "subtotal": r[6],
    } for r in datos]

def total_del_dia():
    return {"total_dia": venta_dao.total_del_dia()}

def resumen_hoy():
    return venta_dao.resumen_del_dia()
