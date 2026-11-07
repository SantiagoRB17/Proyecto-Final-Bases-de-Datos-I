# Datos de quien inició sesión. Se crea en el login y viaja entre ventanas.
class Sesion:
    def __init__(self, usuario, tipo_usuario, bitacora):
        self.usuario = usuario
        self.tipo_usuario = tipo_usuario
        self.bitacora = bitacora
