import pyodbc

from dao.Conexion import obtener_conexion
from model.Producto import Producto


class ProductoDAO:

    def agregar(self, producto):
        sql = """
            INSERT INTO Producto (ProdNombre, ProdDescripcion, ProdPrecio, ProdStock, IDCategoria)
            OUTPUT INSERTED.IDProducto
            VALUES (?, ?, ?, ?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (producto.ProdNombre, producto.ProdDescripcion, producto.ProdPrecio,
                                 producto.ProdStock, producto.IDCategoria))
            producto.IDProducto = cursor.fetchval()
            conexion.commit()
            return producto
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = """
            SELECT IDProducto, ProdNombre, ProdDescripcion, ProdPrecio, ProdStock, IDCategoria
            FROM Producto
            ORDER BY ProdNombre
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_producto(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_producto):
        sql = """
            SELECT IDProducto, ProdNombre, ProdDescripcion, ProdPrecio, ProdStock, IDCategoria
            FROM Producto
            WHERE IDProducto = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_producto,))
            fila = cursor.fetchone()
            return self._fila_a_producto(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, producto):
        sql = """
            UPDATE Producto
            SET ProdNombre = ?, ProdDescripcion = ?, ProdPrecio = ?, ProdStock = ?, IDCategoria = ?
            WHERE IDProducto = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (producto.ProdNombre, producto.ProdDescripcion, producto.ProdPrecio,
                                 producto.ProdStock, producto.IDCategoria, producto.IDProducto))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_producto):
        sql = "DELETE FROM Producto WHERE IDProducto = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_producto,))
            conexion.commit()
        except pyodbc.IntegrityError:
            # La llave foránea de DetalleProveedorProducto impide borrarlo si tiene proveedores.
            raise ValueError("No se puede eliminar el producto: tiene proveedores asociados.")
        finally:
            conexion.close()

    def _fila_a_producto(self, fila):
        return Producto(fila.IDProducto, fila.ProdNombre, fila.ProdDescripcion, fila.ProdPrecio,
                        fila.ProdStock, fila.IDCategoria)
