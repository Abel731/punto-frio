import os
import psycopg2
from dotenv import load_dotenv

class Conexion:
    def __init__(self):
        ruta_envv = os.path.join(os.getcwd(), ".envv")
        if os.path.exists(ruta_envv):
            load_dotenv(ruta_envv)

    def getConexion(self):
        database_url = os.getenv("DATABASE_URL")
        if database_url:
            if "sslmode=" not in database_url:
                sep = "&" if "?" in database_url else "?"
                database_url = f"{database_url}{sep}sslmode=require"
            return psycopg2.connect(database_url)

        return psycopg2.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", "5432")),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
        )
