from Models.seccione import (
    Seccione,
)  # Importa el modelo de Seccion que nuestro molde de datos
from Config.database_config import (
    DatabaseConfig,
)  # Importa la configuración de la base de datos


class SeccionController:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_seccion(self, id_biblioteca, nombre, piso):
        """Crea una nueva seccion en la base de datos."""

        if (
            not self.db.connect()
        ):  # Verifica si la conexión a la base de datos fue exitosa
            return {"error": "No se pudo conectar a la base de datos."}

        query = (
            "INSERT INTO secciones (id_biblioteca, nombre, piso) VALUES (%s, %s, %s)"
        )
        params = (id_biblioteca, nombre, piso)

        cursor = self.db.execute_query(
            query, params
        )  # Ejecuta la consulta para insertar una nueva seccion
        self.db.disconnect()

        return {"message": "Seccion creada exitosamente.", "id": cursor.lastrowid}

    def get_all_secciones(self):
        """Obtiene todas las secciones de la base de datos."""

        if (
            not self.db.connect()
        ):  # Verifica si la conexión a la base de datos fue exitosa
            return {"error": "No se pudo conectar a la base de datos."}

        query = "SELECT * FROM secciones"
        results = self.db.fetch_all(
            query
        )  # Ejecuta la consulta para obtener todas las secciones
        self.db.disconnect()

        secciones = []
        for row in results:
            seccion = Seccione(row[0], row[1], row[2], row[3])
            secciones.append(seccion)

        return secciones

    def get_seccion_by_id(self, id):
        """Obtiene una seccion por su ID."""

        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos."}

        query = "SELECT * FROM secciones WHERE id = %s"
        param = (id,)
        result = self.db.fetch_one(query, param)
        self.db.disconnect()

        if result:
            return Seccione(result[0], result[1], result[2], result[3])

        else:
            return {"error": "Seccion no encontrada."}

    def get_secciones_by_biblioteca(self, id_biblioteca):
        """Obtiene todas las secciones de una biblioteca específica."""

        if not self.db.connect():
            return {"error": "No se pudo conectar a la base de datos."}

        query = """
        SELECT 	b.id,
            b.nombre,
            b.direccion,
            s.nombre,
            s.piso from bibliotecas b
        left join secciones s on b.id = s.id_biblioteca
        where b.id = %s
        order by piso;
"""
        param = (id_biblioteca,)
        results = self.db.fetch_all(query, param)
        self.db.disconnect()

        secciones = []
        for row in results:
            seccion = {
                "id": row[0],
                "nombre_biblioteca": row[1],
                "direccion": row[2],
                "nombre_seccion": row[3],
                "piso": row[4],
            }
            secciones.append(seccion)

        return secciones
