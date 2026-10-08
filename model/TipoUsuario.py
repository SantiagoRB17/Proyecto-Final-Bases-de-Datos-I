class TipoUsuario:
    def __init__(self, IDTipoUsuario=None, TipNombre="", TipDescripcion=""):
        self.IDTipoUsuario = IDTipoUsuario
        self.TipNombre = TipNombre
        self.TipDescripcion = TipDescripcion

    def __str__(self):
        return f"TipoUsuario(IDTipoUsuario={self.IDTipoUsuario}, TipNombre='{self.TipNombre}', TipDescripcion='{self.TipDescripcion}')"
