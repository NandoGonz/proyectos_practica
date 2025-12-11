"""Importamos las librerias que vamos a utilizar en nuestro proyecto"""

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env


class DatabaseConfig:
    """En la clase por medio de los parametros establecemos la conexión a la db"""

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
            print("Conexión a la base de datos exitosa.")
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
        """Retorna la conexión de la bd"""
        return self.connection

    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"[ERROR] al ejecutar la consulta {e}")
            return None

    def fetch_all(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve todos los resultados."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener los datos: {e}")
            return []

    def fetch_one(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve un solo resultado."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"Error al obtener el dato: {e}")
            return None
