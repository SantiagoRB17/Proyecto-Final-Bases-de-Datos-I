import pyodbc

from dao.Conexion import obtener_conexion
from model.DetalleProveedorProducto import DetalleProveedorProducto


# La PK es compuesta (IDProveedor + IDProducto), por eso los métodos que
# buscan una fila reciben los dos IDs y el agregar no usa OUTPUT INSERTED.
class DetalleProveedorProductoDAO:

    def agregar(self, detalle):
        sql = """
            INSERT INTO DetalleProveedorProducto (IDProveedor, IDProducto, DeFechaRegistro, DePrecioProveedor)
            VALUES (?, ?, ?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (detalle.IDProveedor, detalle.IDProducto,
                                 detalle.DeFechaRegistro, detalle.DePrecioProveedor))
            conexion.commit()
            return detalle
        except pyodbc.IntegrityError as error:
            if "PRIMARY KEY" in str(error):
                raise ValueError("Ese proveedor ya tiene registrado ese producto.")
            raise
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = """
            SELECT IDProveedor, IDProducto, DeFechaRegistro, DePrecioProveedor
            FROM DetalleProveedorProducto
            ORDER BY IDProveedor, IDProducto
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_detalle(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_proveedor, id_producto):
        sql = """
            SELECT IDProveedor, IDProducto, DeFechaRegistro, DePrecioProveedor
            FROM DetalleProveedorProducto
            WHERE IDProveedor = ? AND IDProducto = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_proveedor, id_producto))
            fila = cursor.fetchone()
            return self._fila_a_detalle(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, detalle):
        # Solo se editan la fecha y el precio: cambiar el proveedor o el producto
        # sería otra fila (eliminar y agregar).
        sql = """
            UPDATE DetalleProveedorProducto
            SET DeFechaRegistro = ?, DePrecioProveedor = ?
            WHERE IDProveedor = ? AND IDProducto = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (detalle.DeFechaRegistro, detalle.DePrecioProveedor,
                                 detalle.IDProveedor, detalle.IDProducto))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_proveedor, id_producto):
        sql = "DELETE FROM DetalleProveedorProducto WHERE IDProveedor = ? AND IDProducto = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_proveedor, id_producto))
            conexion.commit()
        finally:
            conexion.close()

    def _fila_a_detalle(self, fila):
        return DetalleProveedorProducto(fila.IDProveedor, fila.IDProducto,
                                        fila.DeFechaRegistro, fila.DePrecioProveedor)
