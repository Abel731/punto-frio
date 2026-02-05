from app.dao.referenciales.productos.producto_dao import ProductoDAO

dao = ProductoDAO()

# Crear uno de prueba (podés comentar luego)
dao.crear("Coca-Cola 500ml", 5000, 10)

# Listar
productos = dao.listar()
print("✅ Productos:", productos)