class Usuario:
    # UsrContrasena guarda siempre el hash, nunca la contraseña en texto plano;
    # el hash lo calcula UsuarioService, no esta clase.
    def __init__(self, IDUsuario=None, UsrNombreUsuario="",UsrContrasena="", UsrNombres="", UsrApellidos="", UsrEstado=True, IDTipoUsuario=None):
        self.IDUsuario = IDUsuario
        self.UsrNombreUsuario = UsrNombreUsuario
        self.UsrContrasena = UsrContrasena
        self.UsrNombres = UsrNombres
        self.UsrApellidos = UsrApellidos
        self.UsrEstado = UsrEstado
        self.IDTipoUsuario = IDTipoUsuario

    def __str__(self):
        return (f"Usuario(IDUsuario={self.IDUsuario}, UsrNombreUsuario='{self.UsrNombreUsuario}', "
                f"UsrNombres='{self.UsrNombres}', UsrApellidos='{self.UsrApellidos}', "
                f"UsrEstado={self.UsrEstado}, IDTipoUsuario={self.IDTipoUsuario})")
