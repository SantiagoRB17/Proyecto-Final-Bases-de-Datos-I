import pyodbc

from dao.Conexion import obtener_conexion
from model.Usuario import Usuario


# Este DAO guarda y lee UsrContrasena tal cual llega: el hash lo calcula
# UsuarioService antes de llamar a agregar o editar.
class UsuarioDAO:

    def agregar(self, usuario):
        sql = """
            INSERT INTO Usuario (UsrNombreUsuario, UsrContrasena, UsrNombres, UsrApellidos, UsrEstado, IDTipoUsuario)
            OUTPUT INSERTED.IDUsuario
            VALUES (?, ?, ?, ?, ?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (usuario.UsrNombreUsuario, usuario.UsrContrasena, usuario.UsrNombres,
                                 usuario.UsrApellidos, usuario.UsrEstado, usuario.IDTipoUsuario))
            usuario.IDUsuario = cursor.fetchval()
            conexion.commit()
            return usuario
        except pyodbc.IntegrityError as error:
            if "UQ_Usuario_UsrNombreUsuario" in str(error):
                raise ValueError("Ya existe un usuario con ese nombre de usuario.")
            raise
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = """
            SELECT IDUsuario, UsrNombreUsuario, UsrContrasena, UsrNombres, UsrApellidos, UsrEstado, IDTipoUsuario
            FROM Usuario
            ORDER BY UsrNombreUsuario
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_usuario(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_usuario):
        sql = """
            SELECT IDUsuario, UsrNombreUsuario, UsrContrasena, UsrNombres, UsrApellidos, UsrEstado, IDTipoUsuario
            FROM Usuario
            WHERE IDUsuario = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_usuario,))
            fila = cursor.fetchone()
            return self._fila_a_usuario(fila) if fila else None
        finally:
            conexion.close()

    def consultar_por_nombre_usuario(self, nombre_usuario):
        # Usado por el login: busca al usuario por el nombre con el que inicia sesión.
        sql = """
            SELECT IDUsuario, UsrNombreUsuario, UsrContrasena, UsrNombres, UsrApellidos, UsrEstado, IDTipoUsuario
            FROM Usuario
            WHERE UsrNombreUsuario = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (nombre_usuario,))
            fila = cursor.fetchone()
            return self._fila_a_usuario(fila) if fila else None
        finally:
            conexion.close()

    def contar_por_tipo(self, id_tipo_usuario):
        # Usado por UsuarioService para la regla de un único Administrador.
        sql = "SELECT COUNT(*) FROM Usuario WHERE IDTipoUsuario = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_tipo_usuario,))
            return cursor.fetchval()
        finally:
            conexion.close()

    def editar(self, usuario):
        sql = """
            UPDATE Usuario
            SET UsrNombreUsuario = ?, UsrContrasena = ?, UsrNombres = ?, UsrApellidos = ?,
                UsrEstado = ?, IDTipoUsuario = ?
            WHERE IDUsuario = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (usuario.UsrNombreUsuario, usuario.UsrContrasena, usuario.UsrNombres,
                                 usuario.UsrApellidos, usuario.UsrEstado, usuario.IDTipoUsuario,
                                 usuario.IDUsuario))
            conexion.commit()
        except pyodbc.IntegrityError as error:
            if "UQ_Usuario_UsrNombreUsuario" in str(error):
                raise ValueError("Ya existe un usuario con ese nombre de usuario.")
            raise
        finally:
            conexion.close()

    def eliminar(self, id_usuario):
        # Borrado lógico: el usuario se desactiva (UsrEstado = 0) en vez de
        # borrarse, para conservar su historial en la bitácora.
        sql = "UPDATE Usuario SET UsrEstado = 0 WHERE IDUsuario = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_usuario,))
            conexion.commit()
        finally:
            conexion.close()

    def _fila_a_usuario(self, fila):
        return Usuario(fila.IDUsuario, fila.UsrNombreUsuario, fila.UsrContrasena, fila.UsrNombres,
                       fila.UsrApellidos, fila.UsrEstado, fila.IDTipoUsuario)
