class Proveedor:
    def __init__(self, IDProveedor=None, ProvNit="", ProvNombre="", ProvDireccion="", ProvTelefono="", ProvEmail="", IDCiudad=None):
        self.IDProveedor = IDProveedor
        self.ProvNit = ProvNit
        self.ProvNombre = ProvNombre
        self.ProvDireccion = ProvDireccion
        self.ProvTelefono = ProvTelefono
        self.ProvEmail = ProvEmail
        self.IDCiudad = IDCiudad

    def __str__(self):
        return (f"Proveedor(IDProveedor={self.IDProveedor}, ProvNit='{self.ProvNit}', "
                f"ProvNombre='{self.ProvNombre}', ProvDireccion='{self.ProvDireccion}', "
                f"ProvTelefono='{self.ProvTelefono}', ProvEmail='{self.ProvEmail}', IDCiudad={self.IDCiudad})")
