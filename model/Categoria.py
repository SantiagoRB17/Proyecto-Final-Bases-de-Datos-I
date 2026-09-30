class Categoria:
    def __init__(self, IDCategoria=None, CatNombre="", CatDescripcion=""):
        self.IDCategoria = IDCategoria
        self.CatNombre = CatNombre
        self.CatDescripcion = CatDescripcion

    def __str__(self):
        return f"Categoria(IDCategoria={self.IDCategoria}, CatNombre='{self.CatNombre}', CatDescripcion='{self.CatDescripcion}')"
