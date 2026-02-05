import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Conexion:
    def getConexion(self):
        database_url = os.getenv("DATABASE_URL")

        if not database_url:
            raise Exception("DATABASE_URL no está definida")

        return psycopg2.connect(database_url)
