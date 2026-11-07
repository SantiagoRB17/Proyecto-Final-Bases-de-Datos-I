from dao.Conexion import obtener_conexion


# Consultas del módulo "Consultas y Reportes". Mezclan varias tablas, así que
# no devuelven DTOs: cada método devuelve (encabezados, filas), listo para
# mostrarse en una tabla de la ventana.
class ConsultasDAO:

    # Consultas con JOIN

    def proveedores_con_ciudad_y_productos(self):
        # Proveedor + Ciudad + DetalleProveedorProducto + Producto
        sql = """
            SELECT prov.ProvNombre, ciu.CiuNombre, ciu.CiuDepartamento,
                   prod.ProdNombre, det.DePrecioProveedor
            FROM Proveedor prov
            INNER JOIN Ciudad ciu ON ciu.IDCiudad = prov.IDCiudad
            INNER JOIN DetalleProveedorProducto det ON det.IDProveedor = prov.IDProveedor
            INNER JOIN Producto prod ON prod.IDProducto = det.IDProducto
            ORDER BY prov.ProvNombre, prod.ProdNombre
        """
        return self._ejecutar(sql)

    def productos_con_categoria_y_proveedores(self):
        # Producto + Categoria + DetalleProveedorProducto + Proveedor
        sql = """
            SELECT prod.ProdNombre, cat.CatNombre, prov.ProvNombre,
                   det.DePrecioProveedor, det.DeFechaRegistro
            FROM Producto prod
            INNER JOIN Categoria cat ON cat.IDCategoria = prod.IDCategoria
            INNER JOIN DetalleProveedorProducto det ON det.IDProducto = prod.IDProducto
            INNER JOIN Proveedor prov ON prov.IDProveedor = det.IDProveedor
            ORDER BY prod.ProdNombre, det.DePrecioProveedor
        """
        return self._ejecutar(sql)

    def bitacora_con_usuario_y_rol(self):
        # Bitacora + Usuario + TipoUsuario
        sql = """
            SELECT usr.UsrNombreUsuario, usr.UsrNombres, usr.UsrApellidos, tip.TipNombre,
                   bit.BitFechaIngreso, bit.BitHoraIngreso, bit.BitFechaSalida, bit.BitHoraSalida
            FROM Bitacora bit
            INNER JOIN Usuario usr ON usr.IDUsuario = bit.IDUsuario
            INNER JOIN TipoUsuario tip ON tip.IDTipoUsuario = usr.IDTipoUsuario
            ORDER BY bit.BitFechaIngreso DESC, bit.BitHoraIngreso DESC
        """
        return self._ejecutar(sql)

    # Consultas con subconsulta

    def proveedores_sin_productos(self):
        # Proveedor + DetalleProveedorProducto: proveedores que aún no proveen nada.
        sql = """
            SELECT ProvNit, ProvNombre, ProvTelefono
            FROM Proveedor
            WHERE IDProveedor NOT IN (SELECT IDProveedor FROM DetalleProveedorProducto)
            ORDER BY ProvNombre
        """
        return self._ejecutar(sql)

    def categorias_con_cantidad_de_productos(self):
        # Categoria + Producto: subconsulta correlacionada que cuenta los productos.
        sql = """
            SELECT cat.CatNombre,
                   (SELECT COUNT(*) FROM Producto prod
                    WHERE prod.IDCategoria = cat.IDCategoria) AS CantidadProductos
            FROM Categoria cat
            ORDER BY cat.CatNombre
        """
        return self._ejecutar(sql)

    def _ejecutar(self, sql):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            encabezados = [columna[0] for columna in cursor.description]
            filas = [tuple(fila) for fila in cursor.fetchall()]
            return encabezados, filas
        finally:
            conexion.close()
