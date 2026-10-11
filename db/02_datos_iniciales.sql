-- Proyecto Final - Bases de Datos I
-- Script 2: datos iniciales (roles, usuario administrador y datos de prueba).
-- Ejecutar una sola vez, despues del script 1.

USE ProyectoFinalBD;
GO

-- Roles del sistema.
INSERT INTO TipoUsuario (TipNombre, TipDescripcion) VALUES
    ('Administrador', 'Unico usuario que puede crear usuarios; acceso total'),
    ('Tradicional',   'CRUD completo sobre las entidades (usuario parametrico)'),
    ('Esporadico',    'Solo consultas y reportes');

-- Usuario administrador (la contrasena se guarda como hash SHA-256).
INSERT INTO Usuario (UsrNombreUsuario, UsrContrasena, UsrNombres, UsrApellidos, UsrEstado, IDTipoUsuario)
VALUES (
    'admin',
    '3b612c75a7b5048a435fb6ec81e52ff92d6d795a8b5a9c17070f6a63c97a53b2',
    'Administrador',
    'Del Sistema',
    1,
    (SELECT IDTipoUsuario FROM TipoUsuario WHERE TipNombre = 'Administrador')
);

-- Datos de prueba.
INSERT INTO Ciudad (CiuNombre, CiuDepartamento) VALUES
    ('Armenia',  'Quindio'),
    ('Calarca',  'Quindio'),
    ('Pereira',  'Risaralda'),
    ('Bogota',   'Cundinamarca'),
    ('Medellin', 'Antioquia');

INSERT INTO Categoria (CatNombre, CatDescripcion) VALUES
    ('Alimentos',  'Productos comestibles'),
    ('Bebidas',    'Bebidas y refrescos'),
    ('Aseo',       'Productos de limpieza e higiene'),
    ('Tecnologia', 'Equipos y accesorios electronicos');
GO
