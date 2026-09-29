class Usuario:
    # UsrContrasena siempre debe contener el hash (nunca la contraseña en
    # texto plano); el hashing lo hace UsuarioService, no esta clase.
    def __init__(self, IDUsuario=None, UsrNombre="", UsrContrasena="", UsrNombreCompleto="", UsrTipo="", UsrEstado=True):
        self.IDUsuario = IDUsuario
        self.UsrNombre = UsrNombre
        self.UsrContrasena = UsrContrasena
        self.UsrNombreCompleto = UsrNombreCompleto
        self.UsrTipo = UsrTipo
        self.UsrEstado = UsrEstado

    def __str__(self):
        return (f"Usuario(IDUsuario={self.IDUsuario}, UsrNombre='{self.UsrNombre}', "
                f"UsrNombreCompleto='{self.UsrNombreCompleto}', UsrTipo='{self.UsrTipo}', "
                f"UsrEstado={self.UsrEstado})")
