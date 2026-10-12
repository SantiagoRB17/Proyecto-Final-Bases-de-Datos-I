import pyodbc

from dao.Conexion import obtener_conexion
from model.Categoria import Categoria


class CategoriaDAO:

    def agregar(self, categoria):
        sql = """
            INSERT INTO Categoria (CatNombre, CatDescripcion)
            OUTPUT INSERTED.IDCategoria
            VALUES (?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (categoria.CatNombre, categoria.CatDescripcion))
            categoria.IDCategoria = cursor.fetchval()
            conexion.commit()
            return categoria
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = "SELECT IDCategoria, CatNombre, CatDescripcion FROM Categoria ORDER BY CatNombre"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_categoria(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_categoria):
        sql = "SELECT IDCategoria, CatNombre, CatDescripcion FROM Categoria WHERE IDCategoria = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_categoria,))
            fila = cursor.fetchone()
            return self._fila_a_categoria(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, categoria):
        sql = "UPDATE Categoria SET CatNombre = ?, CatDescripcion = ? WHERE IDCategoria = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (categoria.CatNombre, categoria.CatDescripcion, categoria.IDCategoria))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_categoria):
        sql = "DELETE FROM Categoria WHERE IDCategoria = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_categoria,))
            conexion.commit()
        except pyodbc.IntegrityError:
            # La llave foránea de Producto impide borrar una categoría en uso.
            raise ValueError("No se puede eliminar la categoría: tiene productos asociados.")
        finally:
            conexion.close()

    def _fila_a_categoria(self, fila):
        return Categoria(fila.IDCategoria, fila.CatNombre, fila.CatDescripcion)
