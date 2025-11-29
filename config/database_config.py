import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env


class DatabaseConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.database = os.getenv("DB_NAME")
        self.root = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = os.getenv("DB_PORT")
        self.connection = None

    def connect(self):
        """Establece la conexión a la base de datos MySQL."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.root,
                password=self.password,
                port=self.port,
            )
            return True
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False

    def disconnect(self):
        """Cierra la conexión a la base de datos MySQL."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada.")

    def get_connection(self):
        return self.connection

    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL."""

    def execute_and_commit(self, query, params=None):
        """
        Ejecuta una consulta de modificación (INSERT, UPDATE, DELETE)
        y devuelve el ID del último insert o el número de filas afectadas.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                # Para INSERT, devuelve el ID. Para UPDATE/DELETE, devuelve las filas afectadas.
                if cursor.lastrowid:
                    return cursor.lastrowid
                return cursor.rowcount
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
            return None  # O podrías devolver -1 para indicar un error

    def fetch_all(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve todos los resultados."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener los datos: {e}")
            return []

    def fetch_one(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve un solo resultado."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"Error al obtener el dato: {e}")
            return None
