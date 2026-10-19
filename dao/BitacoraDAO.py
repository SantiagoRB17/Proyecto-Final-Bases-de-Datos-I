from dao.Conexion import obtener_conexion
from model.Bitacora import Bitacora


# Al iniciar sesión se llama a agregar (fecha/hora de salida en None) y se
# guarda el IDBitacora devuelto; al salir se completan la fecha y hora de
# salida en ese mismo objeto y se llama a editar.
class BitacoraDAO:

    def agregar(self, bitacora):
        sql = """
            INSERT INTO Bitacora (IDUsuario, BitFechaIngreso, BitHoraIngreso, BitFechaSalida, BitHoraSalida)
            OUTPUT INSERTED.IDBitacora
            VALUES (?, ?, ?, ?, ?)
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (bitacora.IDUsuario, bitacora.BitFechaIngreso, bitacora.BitHoraIngreso,
                                 bitacora.BitFechaSalida, bitacora.BitHoraSalida))
            bitacora.IDBitacora = cursor.fetchval()
            conexion.commit()
            return bitacora
        finally:
            conexion.close()

    def consultar_todos(self):
        sql = """
            SELECT IDBitacora, IDUsuario, BitFechaIngreso, BitHoraIngreso, BitFechaSalida, BitHoraSalida
            FROM Bitacora
            ORDER BY BitFechaIngreso DESC, BitHoraIngreso DESC
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            return [self._fila_a_bitacora(fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def consultar_por_id(self, id_bitacora):
        sql = """
            SELECT IDBitacora, IDUsuario, BitFechaIngreso, BitHoraIngreso, BitFechaSalida, BitHoraSalida
            FROM Bitacora
            WHERE IDBitacora = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_bitacora,))
            fila = cursor.fetchone()
            return self._fila_a_bitacora(fila) if fila else None
        finally:
            conexion.close()

    def editar(self, bitacora):
        sql = """
            UPDATE Bitacora
            SET IDUsuario = ?, BitFechaIngreso = ?, BitHoraIngreso = ?, BitFechaSalida = ?, BitHoraSalida = ?
            WHERE IDBitacora = ?
        """
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (bitacora.IDUsuario, bitacora.BitFechaIngreso, bitacora.BitHoraIngreso,
                                 bitacora.BitFechaSalida, bitacora.BitHoraSalida, bitacora.IDBitacora))
            conexion.commit()
        finally:
            conexion.close()

    def eliminar(self, id_bitacora):
        sql = "DELETE FROM Bitacora WHERE IDBitacora = ?"
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_bitacora,))
            conexion.commit()
        finally:
            conexion.close()

    def _fila_a_bitacora(self, fila):
        return Bitacora(fila.IDBitacora, fila.IDUsuario, fila.BitFechaIngreso, fila.BitHoraIngreso,
                        fila.BitFechaSalida, fila.BitHoraSalida)
