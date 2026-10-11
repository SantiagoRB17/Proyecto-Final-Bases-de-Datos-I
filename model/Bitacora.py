class Bitacora:
    # BitFechaSalida y BitHoraSalida son None mientras la sesión sigue abierta;
    # se completan al cerrar sesión.
    def __init__(self, IDBitacora=None, IDUsuario=None, BitFechaIngreso=None, BitHoraIngreso=None, BitFechaSalida=None, BitHoraSalida=None):
        self.IDBitacora = IDBitacora
        self.IDUsuario = IDUsuario
        self.BitFechaIngreso = BitFechaIngreso
        self.BitHoraIngreso = BitHoraIngreso
        self.BitFechaSalida = BitFechaSalida
        self.BitHoraSalida = BitHoraSalida

    def __str__(self):
        return (f"Bitacora(IDBitacora={self.IDBitacora}, IDUsuario={self.IDUsuario}, "
                f"BitFechaIngreso={self.BitFechaIngreso}, BitHoraIngreso={self.BitHoraIngreso}, "
                f"BitFechaSalida={self.BitFechaSalida}, BitHoraSalida={self.BitHoraSalida})")
