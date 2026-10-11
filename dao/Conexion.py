import pyodbc

try:
    from dao.config_local import DRIVER, SERVIDOR, BASE_DATOS, USUARIO, CONTRASENA
except ImportError:
    raise ImportError(
        "No se encontró dao/config_local.py. Créalo con los datos de tu SQL Server "
        "local: DRIVER, SERVIDOR, BASE_DATOS, USUARIO y CONTRASENA."
    )


def obtener_conexion():
    # TrustServerCertificate=yes evita el error de certificado SSL que da el
    # driver 18 al conectarse a un SQL Server local.
    cadena_conexion = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVIDOR};"
        f"DATABASE={BASE_DATOS};"
        f"UID={USUARIO};"
        f"PWD={CONTRASENA};"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(cadena_conexion)
