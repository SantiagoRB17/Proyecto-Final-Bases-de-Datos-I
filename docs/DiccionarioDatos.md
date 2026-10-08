# Diccionario de datos - Proyecto Final Bases de Datos I

Tipos pensados para SQL Server. Los nombres de tabla y columna son
exactamente los mismos que ya se usan en los DTOs de `model/` y en el
diagrama E-R, para que el mapeo DAO <-> tabla sea 1 a 1 y no haya que
traducir nombres en ningún punto del código.

## Ciudad

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDCiudad | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado de la ciudad |
| CiuNombre | VARCHAR(100) | NO | | Nombre de la ciudad |
| CiuDepartamento | VARCHAR(100) | NO | | Departamento al que pertenece la ciudad |

## Categoria

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDCategoria | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado de la categoría |
| CatNombre | VARCHAR(100) | NO | | Nombre de la categoría |
| CatDescripcion | VARCHAR(255) | SI | | Descripción libre de la categoría |

## Producto

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDProducto | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado del producto |
| ProdNombre | VARCHAR(100) | NO | | Nombre del producto |
| ProdDescripcion | VARCHAR(255) | SI | | Descripción libre del producto |
| ProdPrecio | DECIMAL(10,2) | NO | | Precio de venta del producto |
| ProdStock | INT | NO | | Unidades disponibles en inventario (default 0) |
| IDCategoria | INT | NO | FK -> Categoria.IDCategoria | Categoría a la que pertenece el producto |

## Proveedor

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDProveedor | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado del proveedor |
| ProvNit | VARCHAR(20) | NO | UNIQUE | NIT del proveedor |
| ProvNombre | VARCHAR(100) | NO | | Nombre o razón comercial del proveedor |
| ProvDireccion | VARCHAR(150) | NO | | Dirección física del proveedor |
| ProvTelefono | VARCHAR(20) | NO | | Teléfono de contacto |
| ProvEmail | VARCHAR(100) | SI | | Correo de contacto |
| IDCiudad | INT | NO | FK -> Ciudad.IDCiudad | Ciudad donde está ubicado el proveedor |

## DetalleProveedorProducto

Tabla intermedia que resuelve la relación N:M entre Proveedor y Producto.
No tiene un ID propio: la llave primaria es compuesta.

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDProveedor | INT | NO | PK compuesta, FK -> Proveedor.IDProveedor | Proveedor que ofrece el producto |
| IDProducto | INT | NO | PK compuesta, FK -> Producto.IDProducto | Producto ofrecido por el proveedor |
| DeFechaRegistro | DATE | NO | | Fecha en que se registró esa relación proveedor-producto |
| DePrecioProveedor | DECIMAL(10,2) | NO | | Precio al que ese proveedor específico ofrece el producto |

## TipoUsuario

Tabla de catálogo de roles. Se modela como tabla (y no como enumeración en el
código) para poder agregar nuevos tipos de cuenta sin modificar el código
fuente. Datos iniciales: Administrador, Tradicional (paramétrico), Esporádico.

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDTipoUsuario | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado del tipo de usuario |
| TipNombre | VARCHAR(30) | NO | UNIQUE | Nombre del rol |
| TipDescripcion | VARCHAR(255) | SI | | Qué permisos tiene ese rol |

## Usuario

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDUsuario | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado del usuario |
| UsrNombreUsuario | VARCHAR(50) | NO | UNIQUE | Nombre de usuario para iniciar sesión |
| UsrContrasena | VARCHAR(255) | NO | | Hash de la contraseña (nunca texto plano, ver UsuarioService) |
| UsrNombres | VARCHAR(75) | NO | | Nombres de la persona (componente del atributo compuesto "Nombre completo") |
| UsrApellidos | VARCHAR(75) | NO | | Apellidos de la persona (componente del atributo compuesto "Nombre completo") |
| UsrEstado | BIT | NO | | 1 = activo, 0 = inactivo (default 1) |
| IDTipoUsuario | INT | NO | FK -> TipoUsuario.IDTipoUsuario | Tipo (rol) del usuario |

## Bitacora

| Columna | Tipo SQL Server | Nulo | Llave | Descripción |
|---|---|---|---|---|
| IDBitacora | INT IDENTITY(1,1) | NO | PK | Identificador autogenerado del registro |
| IDUsuario | INT | NO | FK -> Usuario.IDUsuario | Usuario que generó el ingreso/salida |
| BitFechaIngreso | DATE | NO | | Fecha de inicio de sesión |
| BitHoraIngreso | TIME | NO | | Hora de inicio de sesión |
| BitFechaSalida | DATE | SI | | Fecha de cierre de sesión (NULL mientras sigue conectado) |
| BitHoraSalida | TIME | SI | | Hora de cierre de sesión (NULL mientras sigue conectado) |

## Notas

- `UsrContrasena` se dejó en VARCHAR(255) para que alcance cualquier hash
  (con `hashlib.sha256` seria de 64 caracteres, pero 255 da margen si luego
  usan algo con salt o un algoritmo más largo).
- El tipo de usuario se modela como tabla `TipoUsuario` (decisión del
  profesor: en un curso de bases de datos lo correcto es hacerlo "estilo BD"
  y no con un enum, porque permite agregar roles sin tocar el código).
- Todos los precios (`ProdPrecio`, `DePrecioProveedor`) quedaron en
  `DECIMAL(10,2)` (hasta 99,999,999.99)
