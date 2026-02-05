from werkzeug.security import generate_password_hash
from app.conexion.Conexion import Conexion

# 👇 CAMBIÁ ESTOS DATOS
USUARIO = "admin"
PASSWORD = "19732713"   # después la cambiás por la que quieras

hash_password = generate_password_hash(PASSWORD)

con = Conexion().getConexion()
cur = con.cursor()

cur.execute("""
    INSERT INTO usuarios (usuario, password_hash, activo)
    VALUES (%s, %s, TRUE)
""", (USUARIO, hash_password))

con.commit()
cur.close()
con.close()

print("✅ Usuario admin creado correctamente")
print("Usuario:", USUARIO)
print("Password:", PASSWORD)
