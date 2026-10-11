from dao.Conexion import obtener_conexion

# Prueba rápida: abre la conexión y lista los roles de la tabla TipoUsuario.
conexion = obtener_conexion()
try:
    cursor = conexion.cursor()
    cursor.execute("SELECT IDTipoUsuario, TipNombre FROM TipoUsuario")
    for fila in cursor.fetchall():
        print(fila.IDTipoUsuario, fila.TipNombre)
finally:
    conexion.close()
