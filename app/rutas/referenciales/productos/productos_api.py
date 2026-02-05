from app.dao.referenciales.productos.producto_dao import ProductoDAO

dao = ProductoDAO()

def listar_productos():
    productos = dao.listar()
    return [{"id": p[0], "nombre": p[1], "precio_venta": p[2], "stock": p[3]} for p in productos]

def obtener_producto(producto_id: int):
    p = dao.obtener_por_id(producto_id)
    if not p:
        return None
    return {"id": p[0], "nombre": p[1], "precio_venta": p[2], "stock": p[3]}

def crear_producto(data: dict):
    nombre = (data.get("nombre") or "").strip()
    precio_venta = data.get("precio_venta")
    stock = data.get("stock", 0)

    if nombre == "":
        raise ValueError("El nombre es obligatorio")

    try:
        precio_venta = int(precio_venta)
        stock = int(stock)
    except:
        raise ValueError("Precio y stock deben ser numéricos")

    if precio_venta <= 0:
        raise ValueError("El precio debe ser mayor a 0")
    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    dao.crear(nombre, precio_venta, stock)
    return {"success": True}

def actualizar_producto(producto_id: int, data: dict):
    nombre = (data.get("nombre") or "").strip()
    precio_venta = data.get("precio_venta")
    stock = data.get("stock", 0)

    if nombre == "":
        raise ValueError("El nombre es obligatorio")

    try:
        precio_venta = int(precio_venta)
        stock = int(stock)
    except:
        raise ValueError("Precio y stock deben ser numéricos")

    if precio_venta <= 0:
        raise ValueError("El precio debe ser mayor a 0")
    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    ok = dao.actualizar(producto_id, nombre, precio_venta, stock)
    if not ok:
        return {"success": False, "error": "Producto no encontrado"}
    return {"success": True}

def eliminar_producto(producto_id: int):
    ok = dao.eliminar_logico(producto_id)
    if not ok:
        return {"success": False, "error": "Producto no encontrado"}
    return {"success": True}
