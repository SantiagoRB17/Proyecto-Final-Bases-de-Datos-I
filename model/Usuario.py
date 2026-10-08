class Usuario:
    # UsrContrasena siempre debe contener el hash (nunca la contraseña en
    # texto plano); el hashing lo hace UsuarioService, no esta clase.
    def __init__(self, IDUsuario=None, UsrNombre="", UsrContrasena="", UsrNombreCompleto="", UsrEstado=True, IDTipoUsuario=None):
        self.IDUsuario = IDUsuario
        self.UsrNombre = UsrNombre
        self.UsrContrasena = UsrContrasena
        self.UsrNombreCompleto = UsrNombreCompleto
        self.UsrEstado = UsrEstado
        self.IDTipoUsuario = IDTipoUsuario

    def __str__(self):
        return (f"Usuario(IDUsuario={self.IDUsuario}, UsrNombre='{self.UsrNombre}', "
                f"UsrNombreCompleto='{self.UsrNombreCompleto}', UsrEstado={self.UsrEstado}, "
                f"IDTipoUsuario={self.IDTipoUsuario})")
