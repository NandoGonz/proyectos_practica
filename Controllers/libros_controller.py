from Models.libro import Libro
from Config.database_config import DatabaseConfig


class LibroContoller:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_libro(self, id_seccion, nombre, genero, prologo, isbn, id_biblioteca):
        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos"}

        query = "INSERT INTO bibliotecas (id_seccion, nombre, genero, prologo, isbn, id_biblioteca) VALUES (%s, %s, %s, %s, %s, %s);"
        params = (id_seccion, nombre, genero, prologo, isbn, id_biblioteca)

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()

        return {"message": "Libro creado exitosamente.", "id": cursor.lastrowid}

    def buscar_por_titulo(self, titulo_busqueda):
        query = """
            SELECT DISTINCT 
                    l.nombre AS titulo_libro,
                    l.autores,
                    b.nombre AS biblioteca,
                    s.nombre AS seccion,
                    s.piso
            FROM libros AS l 
            INNER JOIN bibliotecas AS b ON l.id_biblioteca = b.id
            INNER JOIN secciones AS s ON l.id_seccion = s.id
            WHERE l.nombre = %s;"""
        params = (titulo_busqueda,)

        result = self.db.fetch_all(query, params)
        self.db.disconnect()

        r = []
        for row in result:
            biblioteca = {
                "titulo_libre": row[0],
                "autores": row[1],
                "biblioteca": row[2],
                "seccion": row[3],
                "piso": row[4],
            }
            r.append(biblioteca)
        return r
