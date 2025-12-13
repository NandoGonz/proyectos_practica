from Models.libro import Libro
from Config.database_config import DatabaseConfig


class LibroController:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_libro(
        self, id_seccion, nombre, generos, prologo, isbn, autores, id_biblioteca
    ):
        """Crea un nuevo libro en la base de datos"""
        if not self.db.connect():
            return {"[ERROR]": "No se puedo conectar ala base de datos"}

        query = """
        INSERT INTO libros(id_seccion,
            nombre, 
            generos, 
            prologo, 
            isbn, 
            autores, 
            id_biblioteca) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = id_seccion, nombre, generos, prologo, isbn, autores, id_biblioteca

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()
        return {"Message": "libro creado exitosamnete", "id": cursor.lastrowid}

    def buscar_por_libro(self, titulo_busqueda):
        if not self.db.connect():
            return {"[ERROR]": "No se puedo conectar ala base de datos"}

        query = """
        SELECT  l.nombre AS titulo_libro, 
                l.autores,
                b.nombre AS biblioteca,
                s.nombre AS seccion,
                s.piso
        FROM libros AS l
        INNER JOIN bibliotecas b ON l.id_biblioteca = b.id
        INNER JOIN secciones AS s ON l.id_seccion = s.id
        WHERE l.nombre = %s; 
"""
        params = (titulo_busqueda,)

        cursor = self.db.fetch_all(query, params)
        self.db.disconnect()

        return cursor
