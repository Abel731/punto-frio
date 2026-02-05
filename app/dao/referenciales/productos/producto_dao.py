from app.conexion.Conexion import Conexion

class ProductoDAO:
    def listar(self):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT id, nombre, precio_venta, stock
            FROM productos
            WHERE activo = TRUE
            ORDER BY nombre;
        """)
        datos = cur.fetchall()
        cur.close()
        con.close()
        return datos

    def crear(self, nombre: str, precio_venta: int, stock: int):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO productos (nombre, precio_venta, stock)
            VALUES (%s, %s, %s);
        """, (nombre, precio_venta, stock))
        con.commit()
        cur.close()
        con.close()

    def obtener_por_id(self, producto_id: int):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT id, nombre, precio_venta, stock
            FROM productos
            WHERE id = %s AND activo = TRUE;
        """, (producto_id,))
        fila = cur.fetchone()
        cur.close()
        con.close()
        return fila
    
    def actualizar(self, producto_id: int, nombre: str, precio_venta: int, stock: int):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            UPDATE productos
            SET nombre=%s, precio_venta=%s, stock=%s
            WHERE id=%s AND activo=TRUE;
        """, (nombre, precio_venta, stock, producto_id))
        filas = cur.rowcount
        con.commit()
        cur.close()
        con.close()
        return filas > 0
    
    def eliminar_logico(self, producto_id: int):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            UPDATE productos
            SET activo=FALSE
            WHERE id=%s AND activo=TRUE;
        """, (producto_id,))
        filas = cur.rowcount
        con.commit()
        cur.close()
        con.close()
        return filas > 0
    
    def listar_para_venta(self):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT id, nombre, precio_venta, stock
            FROM productos
            WHERE activo=TRUE
            ORDER BY nombre;
        """)
        datos = cur.fetchall()
        cur.close()
        con.close()
        return datos
    
    def obtener_para_venta(self, producto_id: int):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT id, nombre, precio_venta, stock
            FROM productos
            WHERE id=%s AND activo=TRUE;
        """, (producto_id,))
        fila = cur.fetchone()
        cur.close()
        con.close()
        return fila