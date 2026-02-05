from werkzeug.security import generate_password_hash
from app.conexion.Conexion import Conexion

usuario = "admin"
password = ""  # luego cambiás

con = Conexion().getConexion()
cur = con.cursor()
cur.execute("""
  INSERT INTO usuarios (usuario, password_hash)
  VALUES (%s, %s)
  ON CONFLICT (usuario) DO NOTHING;
""", (usuario, generate_password_hash(password)))
con.commit()
cur.close(); con.close()

print("✅ Usuario admin creado")
