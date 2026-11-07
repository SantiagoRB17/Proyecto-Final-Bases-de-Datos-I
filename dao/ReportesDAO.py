from dao.Conexion import obtener_conexion


# Reportes del módulo "Consultas y Reportes". Igual que ConsultasDAO, cada
# método devuelve (encabezados, filas), pero aquí el usuario elige el filtro:
# los valores viajan como parámetros (?) y nunca se pegan dentro del SQL.
class ReportesDAO:

    # ---------- Productos y proveedores ----------

    def productos_de_proveedor(self, id_proveedor):
        sql = """
            SELECT prod.ProdNombre AS Producto, cat.CatNombre AS [Categoría],
                   det.DePrecioProveedor AS [Precio del proveedor],
                   det.DeFechaRegistro AS [Fecha de registro]
            FROM DetalleProveedorProducto det
            INNER JOIN Producto prod ON prod.IDProducto = det.IDProducto
            INNER JOIN Categoria cat ON cat.IDCategoria = prod.IDCategoria
            WHERE det.IDProveedor = ?
            ORDER BY prod.ProdNombre
        """
        return self._ejecutar(sql, (id_proveedor,))

    def proveedores_por_ciudad(self, id_ciudad):
        sql = """
            SELECT prov.ProvNit AS NIT, prov.ProvNombre AS Proveedor,
                   prov.ProvDireccion AS [Dirección], prov.ProvTelefono AS [Teléfono],
                   prov.ProvEmail AS Email
            FROM Proveedor prov
            WHERE prov.IDCiudad = ?
            ORDER BY prov.ProvNombre
        """
        return self._ejecutar(sql, (id_ciudad,))

    def proveedores_de_producto_por_precio(self, id_producto, precio_minimo, precio_maximo):
        sql = """
            SELECT prov.ProvNombre AS Proveedor, ciu.CiuNombre AS Ciudad,
                   det.DePrecioProveedor AS [Precio del proveedor],
                   det.DeFechaRegistro AS [Fecha de registro]
            FROM DetalleProveedorProducto det
            INNER JOIN Proveedor prov ON prov.IDProveedor = det.IDProveedor
            INNER JOIN Ciudad ciu ON ciu.IDCiudad = prov.IDCiudad
            WHERE det.IDProducto = ?
              AND det.DePrecioProveedor BETWEEN ? AND ?
            ORDER BY det.DePrecioProveedor, prov.ProvNombre
        """
        return self._ejecutar(sql, (id_producto, precio_minimo, precio_maximo))

    # ---------- Productos y categorías ----------

    def productos_de_categoria(self, id_categoria):
        sql = """
            SELECT prod.ProdNombre AS Producto, prod.ProdDescripcion AS [Descripción],
                   prod.ProdPrecio AS Precio, prod.ProdStock AS Stock
            FROM Producto prod
            WHERE prod.IDCategoria = ?
            ORDER BY prod.ProdNombre
        """
        return self._ejecutar(sql, (id_categoria,))

    def productos_con_stock_bajo(self, id_categoria, stock_maximo):
        sql = """
            SELECT cat.CatNombre AS [Categoría], prod.ProdNombre AS Producto,
                   prod.ProdPrecio AS Precio, prod.ProdStock AS Stock
            FROM Producto prod
            INNER JOIN Categoria cat ON cat.IDCategoria = prod.IDCategoria
            WHERE prod.IDCategoria = ? AND prod.ProdStock <= ?
            ORDER BY prod.ProdStock, prod.ProdNombre
        """
        return self._ejecutar(sql, (id_categoria, stock_maximo))

    def _ejecutar(self, sql, parametros):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            encabezados = [columna[0] for columna in cursor.description]
            filas = [tuple(fila) for fila in cursor.fetchall()]
            return encabezados, filas
        finally:
            conexion.close()
