class DetalleProveedorProducto:
    # No tiene IDDetalle propio: la PK es compuesta (IDProveedor + IDProducto).
    def __init__(self, IDProveedor=None, IDProducto=None, DeFechaRegistro=None, DePrecioProveedor=0.0):
        self.IDProveedor = IDProveedor
        self.IDProducto = IDProducto
        self.DeFechaRegistro = DeFechaRegistro
        self.DePrecioProveedor = DePrecioProveedor

    def __str__(self):
        return (f"DetalleProveedorProducto(IDProveedor={self.IDProveedor}, IDProducto={self.IDProducto}, "
                f"DeFechaRegistro={self.DeFechaRegistro}, DePrecioProveedor={self.DePrecioProveedor})")
