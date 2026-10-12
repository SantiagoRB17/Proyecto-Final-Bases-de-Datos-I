import pyodbc

from dao.Conexion import obtener_conexion
from model.Ciudad import Ciudad


class CiudadDAO:

    def agregar(self, ciudad):
        # OUTPUT INSERTED devuelve el ID que SQL Server generó con IDENTITY.
        sql = """
            INSERT INTO Ciudad (CiuNombre, CiuDepartamento)
            OUTPUT INSERTED.IDCiudad
            VALUES (?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (ciudad.CiuNombre, ciudad.CiuDepartamento))
            ciudad.IDCiudad = cursor.fetchval()
            conexion.commit()
            return ciudad
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = "SELECT IDCiudad, CiuNombre, CiuDepartamento FROM Ciudad ORDER BY CiuNombre"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_ciudad(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_ciudad):
        sql = "SELECT IDCiudad, CiuNombre, CiuDepartamento FROM Ciudad WHERE IDCiudad = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_ciudad,))
            fila = cursor.fetchone()
            return self._fila_a_ciudad(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, ciudad):
        sql = "UPDATE Ciudad SET CiuNombre = ?, CiuDepartamento = ? WHERE IDCiudad = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (ciudad.CiuNombre, ciudad.CiuDepartamento, ciudad.IDCiudad))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_ciudad):
        sql = "DELETE FROM Ciudad WHERE IDCiudad = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_ciudad,))
            conexion.commit()
        except pyodbc.IntegrityError:
            # La llave foránea de Proveedor impide borrar una ciudad en uso.
            raise ValueError("No se puede eliminar la ciudad: tiene proveedores asociados.")
        finally:
            conexion.close()

    def _fila_a_ciudad(self, fila):
        return Ciudad(fila.IDCiudad, fila.CiuNombre, fila.CiuDepartamento)
