import mysql.connector
from mysql.connector import Error
import os

# from dotenv import load_dotenv


class DatabaseConfig:
    def __init__(self):
        """ "Esstablecimos conexión con la base de datos MySQL"""
        self.host = os.getenv("DB_HOST")
        self.database = os.getenv("DB_NAME")
        self.root = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = os.getenv("DB_PORT")
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                root=self.root,
                password=self.password,
                port=self.port,
            )
            return True
        except Error as e:
            print(f"[ERROR] al conectar a la base de datos {e}")
            return False

    def disconnect(self):
        """Cierra la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada")

    def get_connection(self):
        """Retormanos la conexión"""
        return self.connection

    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"[ERROR] al ejecutar la cosulta: {e}")

    def fetch_all(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve todos los resultados"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"[ERRO] al obtener el dato: {e}")
            return None

    def fetch_one(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve un solo  resultado"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"[ERROR] al obtener el dato: {e}")
