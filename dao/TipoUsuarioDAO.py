import pyodbc

from dao.Conexion import obtener_conexion
from model.TipoUsuario import TipoUsuario


class TipoUsuarioDAO:

    def agregar(self, tipo_usuario):
        sql = """
            INSERT INTO TipoUsuario (TipNombre, TipDescripcion)
            OUTPUT INSERTED.IDTipoUsuario
            VALUES (?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (tipo_usuario.TipNombre, tipo_usuario.TipDescripcion))
            tipo_usuario.IDTipoUsuario = cursor.fetchval()
            conexion.commit()
            return tipo_usuario
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = "SELECT IDTipoUsuario, TipNombre, TipDescripcion FROM TipoUsuario ORDER BY TipNombre"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_tipo_usuario(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_tipo_usuario):
        sql = "SELECT IDTipoUsuario, TipNombre, TipDescripcion FROM TipoUsuario WHERE IDTipoUsuario = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_tipo_usuario,))
            fila = cursor.fetchone()
            return self._fila_a_tipo_usuario(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, tipo_usuario):
        sql = "UPDATE TipoUsuario SET TipNombre = ?, TipDescripcion = ? WHERE IDTipoUsuario = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (tipo_usuario.TipNombre, tipo_usuario.TipDescripcion,
                                 tipo_usuario.IDTipoUsuario))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_tipo_usuario):
        sql = "DELETE FROM TipoUsuario WHERE IDTipoUsuario = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_tipo_usuario,))
            conexion.commit()
        except pyodbc.IntegrityError:
            # La llave foránea de Usuario impide borrar un rol asignado.
            raise ValueError("No se puede eliminar el tipo de usuario: tiene usuarios asociados.")
        finally:
            conexion.close()

    def _fila_a_tipo_usuario(self, fila):
        return TipoUsuario(fila.IDTipoUsuario, fila.TipNombre, fila.TipDescripcion)
