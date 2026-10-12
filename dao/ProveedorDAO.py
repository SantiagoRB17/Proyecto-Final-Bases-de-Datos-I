import pyodbc

from dao.Conexion import obtener_conexion
from model.Proveedor import Proveedor


class ProveedorDAO:

    def agregar(self, proveedor):
        sql = """
            INSERT INTO Proveedor (ProvNit, ProvNombre, ProvDireccion, ProvTelefono, ProvEmail, IDCiudad)
            OUTPUT INSERTED.IDProveedor
            VALUES (?, ?, ?, ?, ?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (proveedor.ProvNit, proveedor.ProvNombre, proveedor.ProvDireccion,
                                 proveedor.ProvTelefono, proveedor.ProvEmail, proveedor.IDCiudad))
            proveedor.IDProveedor = cursor.fetchval()
            conexion.commit()
            return proveedor
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = """
            SELECT IDProveedor, ProvNit, ProvNombre, ProvDireccion, ProvTelefono, ProvEmail, IDCiudad
            FROM Proveedor
            ORDER BY ProvNombre
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_proveedor(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_proveedor):
        sql = """
            SELECT IDProveedor, ProvNit, ProvNombre, ProvDireccion, ProvTelefono, ProvEmail, IDCiudad
            FROM Proveedor
            WHERE IDProveedor = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_proveedor,))
            fila = cursor.fetchone()
            return self._fila_a_proveedor(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, proveedor):
        sql = """
            UPDATE Proveedor
            SET ProvNit = ?, ProvNombre = ?, ProvDireccion = ?, ProvTelefono = ?, ProvEmail = ?, IDCiudad = ?
            WHERE IDProveedor = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (proveedor.ProvNit, proveedor.ProvNombre, proveedor.ProvDireccion,
                                 proveedor.ProvTelefono, proveedor.ProvEmail, proveedor.IDCiudad,
                                 proveedor.IDProveedor))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_proveedor):
        sql = "DELETE FROM Proveedor WHERE IDProveedor = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_proveedor,))
            conexion.commit()
        except pyodbc.IntegrityError:
            # La llave foránea de DetalleProveedorProducto impide borrarlo si provee productos.
            raise ValueError("No se puede eliminar el proveedor: tiene productos asociados.")
        finally:
            conexion.close()

    def _fila_a_proveedor(self, fila):
        return Proveedor(fila.IDProveedor, fila.ProvNit, fila.ProvNombre, fila.ProvDireccion,
                         fila.ProvTelefono, fila.ProvEmail, fila.IDCiudad)
