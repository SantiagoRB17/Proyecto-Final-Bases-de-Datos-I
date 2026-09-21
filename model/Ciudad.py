class Ciudad:
    def __init__(self, IDCiudad=None, CiuNombre="", CiuDepartamento=""):
        self.IDCiudad = IDCiudad
        self.CiuNombre = CiuNombre
        self.CiuDepartamento = CiuDepartamento

    def __str__(self):
        return f"Ciudad(IDCiudad={self.IDCiudad}, CiuNombre='{self.CiuNombre}', CiuDepartamento='{self.CiuDepartamento}')"