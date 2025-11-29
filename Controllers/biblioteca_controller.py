from Models.biblioteca import Biblioteca
from Config.database_config import DatabaseConfig


class BibliotecaController:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_biblioteca(self, nombre, direccion):
        """Crea una nueva biblioteca en la base datos"""

        # Conectar
        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos"}

        # Consulta SQL corregida
        query = "INSERT INTO bibliotecas (nombre, direccion) VALUES (%s, %s);"
        params = (nombre, direccion)

        cursor = self.db.execute_query(query, params)

        if cursor is None:
            self.db.disconnect()
            return {"error": "La consulta falló. No se pudo insertar la biblioteca"}

        # Obtener ID
        last_id = cursor.lastrowid
        cursor.close()

        # Cerrar conexión
        self.db.disconnect()

        return {"message": "Biblioteca creada exitosamente.", "id": last_id}

    # Consultamos todo
    def get_all_bibliotecas(self):
        if not self.db.connect():
            return {"[ERROR]": "No se pudo conectar a la base de datos."}

        query = "SELECT * FROM bibliotecas ORDER BY nombre;"
        result = self.db.fetch_all(query)
        self.db.disconnect()

        bibliotecas = []
        for row in result:
            biblioteca = Biblioteca(row["id"], row["nombre"], row["direccion"])
            bibliotecas.append(biblioteca)
        return bibliotecas

    def get_biblioteca_by_id(self, id):

        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos"}

        query = "SELECT * FROM bibliotecas WHERE id = %s;"
        param = (id,)
        result = self.db.fetch_one(query, param)
        self.db.disconnect()

        if result:
            return Biblioteca(result["id"], result["nombre"], result["direccion"])
        else:
            return {"[ERROR]": "Biblioteca no encontrada"}

    def update_biblioteca(self, id, nombre, direccion):
        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos"}

        query = "UPDATE bibliotecas SET nombre = %s, direccion = %s WHERE id = %s; "
        params = (nombre, direccion, id)

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()
        return cursor is not None and cursor.rowcount > 0

    def delete_biblioteca(self, id):
        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos"}

        query = "DELETE FROM bibliotecas WHERE id = %s;"
        param = (id,)

        cursor = self.db.execute_query(query, param)
        self.db.disconnect()

        return cursor is not None and cursor.rowcount > 0
