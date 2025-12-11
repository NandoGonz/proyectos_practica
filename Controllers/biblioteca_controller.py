from Models.biblioteca import Biblioteca
from Config.database_config import DatabaseConfig


class BibliotecaController:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_bibliteca(self, nombre, direccion):
        """Crea una nueva biblioteca en la base de datos"""
        if not self.db.connect():
            return {"[ERROR]": "No se pudo conectar a la base de datos"}

        query = "INSERT INTO bibliotecas(nombre, direccion) VALUES (%s, %s)"
        params = nombre, direccion

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()

        return {"message": "Biblioteca creada exitosamente.", "id": cursor.lastrowid}

    def get_all_bibliotecas(self):
        if not self.db.connect():
            return {"[ERROR]": "No se pudo conectar a la base de datos"}

        query = "SELECT * FROM bibliotecas ORDER BY nombre"
        result = self.db.fetch_all(query)
        self.db.disconnect()

        bibliotecas = []
        for row in result:
            biblioteca = Biblioteca(row[0], row[1], row[2])
            bibliotecas.append(biblioteca)
        return bibliotecas
