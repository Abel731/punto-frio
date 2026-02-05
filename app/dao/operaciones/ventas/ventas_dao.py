from app.conexion.Conexion import Conexion

class VentaDAO:
    def crear_venta_simple(self, producto_id: int, cantidad: int, metodo_pago: str):
        if metodo_pago not in ("efectivo", "transferencia"):
            raise ValueError("Método de pago inválido")

        con = Conexion().getConexion()
        try:
            cur = con.cursor()

            cur.execute("""
                SELECT precio_venta, stock
                FROM productos
                WHERE id=%s AND activo=TRUE
                FOR UPDATE;
            """, (producto_id,))
            fila = cur.fetchone()
            if not fila:
                raise ValueError("Producto no encontrado")

            precio_venta, stock = fila
            if cantidad <= 0:
                raise ValueError("Cantidad inválida")
            if stock < cantidad:
                raise ValueError("Stock insuficiente")

            subtotal = precio_venta * cantidad

            # insertar venta con método
            cur.execute("""
                INSERT INTO ventas (total, metodo_pago)
                VALUES (0, %s)
                RETURNING id;
            """, (metodo_pago,))
            venta_id = cur.fetchone()[0]

            # detalle
            cur.execute("""
                INSERT INTO venta_detalle
                (venta_id, producto_id, cantidad, precio_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s);
            """, (venta_id, producto_id, cantidad, precio_venta, subtotal))

            # total
            cur.execute("UPDATE ventas SET total=%s WHERE id=%s;", (subtotal, venta_id))

            # descontar stock
            cur.execute("UPDATE productos SET stock = stock - %s WHERE id=%s;", (cantidad, producto_id))

            con.commit()
            cur.close()
            return venta_id

        except Exception:
            con.rollback()
            raise
        finally:
            con.close()

    def ventas_del_dia(self):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT v.id, v.fecha, v.total,
                   p.nombre, d.cantidad, d.precio_unitario, d.subtotal
            FROM ventas v
            JOIN venta_detalle d ON d.venta_id = v.id
            JOIN productos p ON p.id = d.producto_id
            WHERE v.fecha::date = CURRENT_DATE
            ORDER BY v.fecha DESC, v.id DESC;
        """)
        datos = cur.fetchall()
        cur.close()
        con.close()
        return datos

    def total_del_dia(self):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT COALESCE(SUM(total), 0)
            FROM ventas
            WHERE fecha::date = CURRENT_DATE;
        """)
        total = cur.fetchone()[0]
        cur.close()
        con.close()
        return total

    def resumen_del_dia(self):
        con = Conexion().getConexion()
        cur = con.cursor()
        cur.execute("""
            SELECT
              COALESCE(SUM(total),0) AS total_dia,
              COALESCE(SUM(CASE WHEN metodo_pago='efectivo' THEN total ELSE 0 END),0) AS total_efectivo,
              COALESCE(SUM(CASE WHEN metodo_pago='transferencia' THEN total ELSE 0 END),0) AS total_transferencia
            FROM ventas
            WHERE fecha::date = CURRENT_DATE;
        """)
        r = cur.fetchone()
        cur.close()
        con.close()
        return {
            "total_dia": r[0],
            "total_efectivo": r[1],
            "total_transferencia":  r[2]
        }