from Models.seccion import Seccion
from Config.database_config import DatabaseConfig


class SeccionController:
    def __init__(self):
        self.db = DatabaseConfig()

    def create_seccion(self, id_biblioteca, nombre, piso):
        if not self.db.connect():
            return {"[ERROR]": "No se puede conectar a la base de datos"}

        query = "INSERT INTO secciones(id_biblioteca, nombre, piso) VALUES(%s, %s, %s)"
        params = (id_biblioteca, nombre, piso)

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()

        return {"Message": "Sección creada con el exitosamnete", "id": cursor.lastrowid}

    def get_all_secciones(self):
        """Muestra todas las secciones de la biblioteca"""
        if not self.db.connect():
            return {"[ERROR]": "No se puedo conectar ala base de datos"}

        query = "SELECT * FROM secciones"
        result = self.db.fetch_all(query)

        secciones = []
        for row in result:
            seccion = Seccion(row[0], row[1], row[2], row[3])
            secciones.append(seccion)
        return secciones

    def get_seccion_by_id(self, id):
        if not self.db.connect():
            return {"[ERROR]": "No se puedo conectar ala base de datos"}

        query = "SELECT * FROM secciones WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        self.db.disconnect()

        if result:
            return Seccion(result[0], result[1], result[2], result[3])
        else:
            return {"error": "No se pudo conectar a la base de datos"}

    def get_secciones_by_bibliotecas(self, id_biblioteca):
        """Obtiene todas las secciones de un biblioteca especificada"""
        if not self.db.connect():
            return {"[ERROR]": "No se puedo conectar a la base de datos"}

        query = """
        SELECT  b.id,
            b.nombre,
            b.direccion,
            s.nombre,
            s.piso
        FROM bibliotecas AS b
        LEFT JOIN secciones AS S ON b.id = s.id_biblioteca
        WHERE b.id = %s
        ORDER BY piso;
        """
        params = (id_biblioteca,)
        results = self.db.fetch_all(query, params)
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

    def update_seccion(self, nuevo_nombre, nuevo_piso, id):
        if not self.db.connect():
            return {"[ERROR]": "No se pudo conectar a la base de datos."}

        query = "UPDATE secciones SET nombre = %s, piso = %s WHERE id = %s;"
        params = (nuevo_nombre, nuevo_piso, id)

        cursor = self.db.execute_query(query, params)
        self.db.disconnect()

        print(cursor)
        return cursor is not None

    def delete_seccion(self, id):
        if not self.db.connect():
            return {"[ERROR]": "No se pudo conectar a la base de datos."}

        query = "DELETE FROM secciones WHERE id = %s"
        params = (id,)

        cursor = self.db.execute_query(query, params)

        if cursor is not None:
            if cursor.rowcount > 0:
                self.db.disconnect()
                return {
                    "source": True,
                    "message": f"seccion con el id {id} se elimino corretamente",
                }
            else:
                self.db.disconnect()
                return {
                    "source": False,
                    "message": f"no esxiste ninguna seccion con el id {id}",
                }
