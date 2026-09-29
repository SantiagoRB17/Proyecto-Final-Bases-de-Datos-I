class Producto:
    def __init__(self, IDProducto=None, ProdNombre="", ProdDescripcion="", ProdPrecio=0.0, ProdStock=0, IDCategoria=None):
        self.IDProducto = IDProducto
        self.ProdNombre = ProdNombre
        self.ProdDescripcion = ProdDescripcion
        self.ProdPrecio = ProdPrecio
        self.ProdStock = ProdStock
        self.IDCategoria = IDCategoria

    def __str__(self):
        return (f"Producto(IDProducto={self.IDProducto}, ProdNombre='{self.ProdNombre}', "
                f"ProdDescripcion='{self.ProdDescripcion}', ProdPrecio={self.ProdPrecio}, "
                f"ProdStock={self.ProdStock}, IDCategoria={self.IDCategoria})")
