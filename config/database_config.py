"""En esta carpeta crearemos la conexión desde  python a la base de datos
con el fin de controlar todas las modificaciones desde python importamos la libreria para establecer la conexion
y también un alibreria para capturar las excepciones de mySQL en python y aque estas son distintas
en su mayoria"""

import os  # esta libreria la importamos para poder navegar entre archivos
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables de entorno desde el archivo .env


# creamos una clase para establecer la conexión a la base de datos
class DatabaseConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST")  # es los mismo 127.0.1(cuando es local)
        self.database = os.getenv(
            "DB_NAME"
        )  # esta es la forma de llamar a nuestras variables para establecer la conexión
        self.root = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = os.getenv("DB_PORT")
        self.connection = None

    # Creamos la conexión
    def connect(self):
        """Establecimso una conexión con nuestra base datos MYSQL"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.root,
                password=self.password,
                port=self.port,
            )
        except Error as e:
            print(f"[ERROR] al conectar la base de datos {e}")
            return False

    # creamos un metodo para desconectarnos de la base de datos
    def disconnect(self):
        """Cierra la conexión a la base ded datos MYSQL"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("La conexión a la base de datos cerrada")

    # Retonamos la conexión
    def get_conecction(self):
        """Devuelve la conexión activa de la base de datos"""
        return self.connection

    # Ahora ejecutaremso las querys
    def execute_query(self, query, params=None):
        """ejecuta una consulta SQL"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"[ERROR] al ejecutar la consulta {e}")
            return None

    # Podemos realizar un fetchall que devuelva mucha información
    def fetch_all(self, query, params=None):
        """Ejecuta una consuta SQL y devuelve todos los resultados"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"[ERROR] al obtener los datos {e}")
            return None

    def fetch_one(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve un solo resultado"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"[ERROR] al obtener los datos {e}")
            return None
