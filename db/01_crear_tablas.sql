-- Proyecto Final - Bases de Datos I
-- Script 1: crea la base de datos y las 8 tablas en SQL Server.
-- Nombres y tipos segun docs/DiccionarioDatos.md.
-- Las llaves foraneas no usan ON DELETE CASCADE: SQL Server rechaza borrar
-- una fila que tenga filas hijas, y el DAO debe capturar ese error.

IF DB_ID('ProyectoFinalBD') IS NULL
    CREATE DATABASE ProyectoFinalBD;
GO

USE ProyectoFinalBD;
GO

-- Reinicio de la estructura (BORRA TODOS LOS DATOS): descomentar este bloque.
-- Se eliminan primero las tablas hijas por las llaves foraneas.
-- DROP TABLE IF EXISTS Bitacora;
-- DROP TABLE IF EXISTS DetalleProveedorProducto;
-- DROP TABLE IF EXISTS Usuario;
-- DROP TABLE IF EXISTS Producto;
-- DROP TABLE IF EXISTS Proveedor;
-- DROP TABLE IF EXISTS TipoUsuario;
-- DROP TABLE IF EXISTS Categoria;
-- DROP TABLE IF EXISTS Ciudad;
-- GO

-- ---------- Tablas independientes ----------

CREATE TABLE Ciudad (
    IDCiudad        INT IDENTITY(1,1) NOT NULL,
    CiuNombre       VARCHAR(100)      NOT NULL,
    CiuDepartamento VARCHAR(100)      NOT NULL,
    CONSTRAINT PK_Ciudad PRIMARY KEY (IDCiudad)
);

CREATE TABLE Categoria (
    IDCategoria    INT IDENTITY(1,1) NOT NULL,
    CatNombre      VARCHAR(100)      NOT NULL,
    CatDescripcion VARCHAR(255)      NULL,
    CONSTRAINT PK_Categoria PRIMARY KEY (IDCategoria)
);

CREATE TABLE TipoUsuario (
    IDTipoUsuario  INT IDENTITY(1,1) NOT NULL,
    TipNombre      VARCHAR(30)       NOT NULL,
    TipDescripcion VARCHAR(255)      NULL,
    CONSTRAINT PK_TipoUsuario PRIMARY KEY (IDTipoUsuario),
    CONSTRAINT UQ_TipoUsuario_TipNombre UNIQUE (TipNombre)
);

-- ---------- Tablas con llaves foraneas ----------

CREATE TABLE Proveedor (
    IDProveedor   INT IDENTITY(1,1) NOT NULL,
    ProvNit       VARCHAR(20)       NOT NULL,
    ProvNombre    VARCHAR(100)      NOT NULL,
    ProvDireccion VARCHAR(150)      NOT NULL,
    ProvTelefono  VARCHAR(20)       NOT NULL,
    ProvEmail     VARCHAR(100)      NULL,
    IDCiudad      INT               NOT NULL,
    CONSTRAINT PK_Proveedor PRIMARY KEY (IDProveedor),
    CONSTRAINT UQ_Proveedor_ProvNit UNIQUE (ProvNit),
    CONSTRAINT FK_Proveedor_Ciudad FOREIGN KEY (IDCiudad) REFERENCES Ciudad (IDCiudad)
);

CREATE TABLE Producto (
    IDProducto      INT IDENTITY(1,1) NOT NULL,
    ProdNombre      VARCHAR(100)      NOT NULL,
    ProdDescripcion VARCHAR(255)      NULL,
    ProdPrecio      DECIMAL(10,2)     NOT NULL,
    ProdStock       INT               NOT NULL CONSTRAINT DF_Producto_ProdStock DEFAULT 0,
    IDCategoria     INT               NOT NULL,
    CONSTRAINT PK_Producto PRIMARY KEY (IDProducto),
    CONSTRAINT FK_Producto_Categoria FOREIGN KEY (IDCategoria) REFERENCES Categoria (IDCategoria)
);

CREATE TABLE Usuario (
    IDUsuario        INT IDENTITY(1,1) NOT NULL,
    UsrNombreUsuario VARCHAR(50)       NOT NULL,
    UsrContrasena    VARCHAR(255)      NOT NULL,  -- hash, nunca texto plano
    UsrNombres       VARCHAR(75)       NOT NULL,
    UsrApellidos     VARCHAR(75)       NOT NULL,
    UsrEstado        BIT               NOT NULL CONSTRAINT DF_Usuario_UsrEstado DEFAULT 1,
    IDTipoUsuario    INT               NOT NULL,
    CONSTRAINT PK_Usuario PRIMARY KEY (IDUsuario),
    CONSTRAINT UQ_Usuario_UsrNombreUsuario UNIQUE (UsrNombreUsuario),
    CONSTRAINT FK_Usuario_TipoUsuario FOREIGN KEY (IDTipoUsuario) REFERENCES TipoUsuario (IDTipoUsuario)
);

-- Tabla intermedia de la relacion N:M Proveedor-Producto (PK compuesta).
CREATE TABLE DetalleProveedorProducto (
    IDProveedor       INT           NOT NULL,
    IDProducto        INT           NOT NULL,
    DeFechaRegistro   DATE          NOT NULL,
    DePrecioProveedor DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_DetalleProveedorProducto PRIMARY KEY (IDProveedor, IDProducto),
    CONSTRAINT FK_Detalle_Proveedor FOREIGN KEY (IDProveedor) REFERENCES Proveedor (IDProveedor),
    CONSTRAINT FK_Detalle_Producto  FOREIGN KEY (IDProducto)  REFERENCES Producto (IDProducto)
);

CREATE TABLE Bitacora (
    IDBitacora      INT IDENTITY(1,1) NOT NULL,
    IDUsuario       INT               NOT NULL,
    BitFechaIngreso DATE              NOT NULL,
    BitHoraIngreso  TIME              NOT NULL,
    BitFechaSalida  DATE              NULL,  -- NULL mientras la sesion sigue abierta
    BitHoraSalida   TIME              NULL,
    CONSTRAINT PK_Bitacora PRIMARY KEY (IDBitacora),
    CONSTRAINT FK_Bitacora_Usuario FOREIGN KEY (IDUsuario) REFERENCES Usuario (IDUsuario)
);
GO
