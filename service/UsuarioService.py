import hashlib
from datetime import datetime

from dao.BitacoraDAO import BitacoraDAO
from dao.ConsultasDAO import ConsultasDAO
from dao.TipoUsuarioDAO import TipoUsuarioDAO
from dao.UsuarioDAO import UsuarioDAO
from model.Bitacora import Bitacora
from service.Sesion import Sesion


class UsuarioService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()
        self.tipo_usuario_dao = TipoUsuarioDAO()
        self.bitacora_dao = BitacoraDAO()
        self.consultas_dao = ConsultasDAO()

    # Sesión

    def iniciar_sesion(self, nombre_usuario, contrasena):
        usuario = self.usuario_dao.consultar_por_nombre_usuario(nombre_usuario)
        # El mismo mensaje en ambos casos, para no revelar qué usuarios existen.
        if usuario is None or usuario.UsrContrasena != self._calcular_hash(contrasena):
            raise ValueError("Usuario o contraseña incorrectos.")
        if not usuario.UsrEstado:
            raise ValueError("El usuario está inactivo.")

        ahora = datetime.now()
        bitacora = Bitacora(None, usuario.IDUsuario, ahora.date(), ahora.time().replace(microsecond=0))
        self.bitacora_dao.agregar(bitacora)
        tipo_usuario = self.tipo_usuario_dao.consultar_por_id(usuario.IDTipoUsuario)
        return Sesion(usuario, tipo_usuario, bitacora)

    def cerrar_sesion(self, sesion):
        ahora = datetime.now()
        sesion.bitacora.BitFechaSalida = ahora.date()
        sesion.bitacora.BitHoraSalida = ahora.time().replace(microsecond=0)
        self.bitacora_dao.editar(sesion.bitacora)

    # Permisos

    def es_administrador(self, id_usuario):
        usuario = self.consultar_usuario_por_id(id_usuario)
        return self._es_tipo_administrador(usuario.IDTipoUsuario)

    def puede_modificar(self, sesion):
        # Administrador y Tradicional hacen CRUD; Esporádico solo consulta.
        return sesion.tipo_usuario.TipNombre.lower() in ("administrador", "tradicional")

    # Gestión de usuarios

    def agregar_usuario(self, usuario_actual, nuevo_usuario, contrasena):
        self._exigir_administrador(usuario_actual, "agregar un nuevo usuario")
        es_admin = self._es_tipo_administrador(nuevo_usuario.IDTipoUsuario)
        if es_admin and self.usuario_dao.contar_por_tipo(nuevo_usuario.IDTipoUsuario) > 0:
            raise ValueError("Ya existe un usuario con el rol de Administrador. No se puede agregar otro.")
        nuevo_usuario.UsrContrasena = self._calcular_hash(contrasena)
        return self.usuario_dao.agregar(nuevo_usuario)

    def consultar_todos_usuarios(self, usuario_actual):
        self._exigir_administrador(usuario_actual, "consultar todos los usuarios")
        return self.usuario_dao.consultar_todos()

    def consultar_usuario_por_id(self, id_usuario):
        usuario = self.usuario_dao.consultar_por_id(id_usuario)
        if usuario is None:
            raise ValueError(f"No se encontró un usuario con ID {id_usuario}")
        return usuario

    def editar_usuario(self, usuario_actual, usuario, contrasena_nueva=None):
        self._exigir_administrador(usuario_actual, "editar usuarios")
        registrado = self.consultar_usuario_por_id(usuario.IDUsuario)
        era_admin = self._es_tipo_administrador(registrado.IDTipoUsuario)
        sera_admin = self._es_tipo_administrador(usuario.IDTipoUsuario)
        if sera_admin and not era_admin:
            raise ValueError("Ya existe un usuario con el rol de Administrador. No se puede agregar otro.")
        if era_admin and (not sera_admin or not usuario.UsrEstado):
            raise ValueError("El Administrador no se puede desactivar ni cambiar de rol.")

        if contrasena_nueva:
            usuario.UsrContrasena = self._calcular_hash(contrasena_nueva)
        else:
            usuario.UsrContrasena = registrado.UsrContrasena
        self.usuario_dao.editar(usuario)

    def eliminar_usuario(self, usuario_actual, id_usuario):
        self._exigir_administrador(usuario_actual, "eliminar usuarios")
        if self.es_administrador(id_usuario):
            raise ValueError("El Administrador no se puede eliminar.")
        self.usuario_dao.eliminar(id_usuario)

    def consultar_tipos_usuario(self, usuario_actual):
        self._exigir_administrador(usuario_actual, "consultar los tipos de usuario")
        return self.tipo_usuario_dao.consultar_todos()

    def consultar_bitacora(self, usuario_actual):
        self._exigir_administrador(usuario_actual, "consultar la bitácora")
        return self.consultas_dao.bitacora_con_usuario_y_rol()

    # Métodos internos

    def _exigir_administrador(self, usuario_actual, accion):
        if not self.es_administrador(usuario_actual.IDUsuario):
            raise PermissionError(f"No tiene permisos para {accion}.")

    def _es_tipo_administrador(self, id_tipo_usuario):
        tipo_usuario = self.tipo_usuario_dao.consultar_por_id(id_tipo_usuario)
        return tipo_usuario.TipNombre.lower() == "administrador"

    def _calcular_hash(self, contrasena):
        return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()
