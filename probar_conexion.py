from app.conexion.Conexion import Conexion
import traceback

try:
    con = Conexion().getConexion()
    cur = con.cursor()
    cur.execute("SELECT 1;")
    print("✅ Conexión OK:", cur.fetchone())
    cur.close()
    con.close()
except Exception as e:
    print("❌ Error de conexión (repr):", repr(e))
    print("❌ Error de conexión (str):", str(e))
    print("\n--- TRACEBACK COMPLETO ---")
    traceback.print_exc()
