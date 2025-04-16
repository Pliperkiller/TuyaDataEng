-- Corregimos "Açtiva" => "Activa"
INSERT INTO cliente
(nombre, identificacion, tipo_documento, clasificacion, tipo_tarjeta, fecha_apertura_tarjeta, estado_tarjeta)
VALUES
('Juan Pérez',         '2C3D4E5F6G7H8I9J0', 'DNI',       'Personal',    'Crédito', '2023-01-15', 'Activa'),
('María García',       '2M3N4O5P6Q7R8S9T0', 'Pasaporte', 'Empresarial', 'Débito',  '2022-11-20', 'Activa'),
('Carlos Rodríguez',   '2W3X4Y5Z6A7B8C9D0', 'DNI',       'Personal',    'Crédito', '2021-05-30', 'Inactiva'),
('Ana Martínez',       '2G3H4I5J6K7L8M9N0', 'Cédula',    'Empresarial', 'Débito',  '2020-08-25', 'Activa'),
('Luis Hernández',     '2Q3R4S5T6U7V8W9X0', 'Pasaporte', 'Personal',    'Crédito', '2019-12-10', 'Activa'),
('Laura López',        '2A3B4C5D6E7F8G9H0', 'DNI',       'Empresarial', 'Débito',  '2018-07-14', 'Inactiva'),
('Pedro González',     '2K3L4M5N6O7P8Q9R0', 'Cédula',    'Personal',    'Crédito', '2017-03-22', 'Activa'),
('Sofía Sánchez',      '2U3V4W5X6Y7Z8A9B0', 'DNI',       'Empresarial', 'Débito',  '2016-09-05', 'Activa'),
('Marta Torres',       '2O3P4Q5R6S7T8U9V0', 'Cédula',    'Empresarial', 'Débito',  '2014-06-27', 'Activa'),
('Jorge Flores',       '2Y3Z4A5B6C7D8E9F0', 'Pasaporte', 'Personal',    'Crédito', '2013-04-09', 'Activa'),
('Elena Ruiz',         '2I3J4K5L6M7N8O9P0', 'DNI',       'Empresarial', 'Débito',  '2012-10-31', 'Inactiva'),
('Andrés Jiménez',     '2S3T4U5V6W7X8Y9Z0', 'Cédula',    'Personal',    'Crédito', '2011-02-13', 'Activa'),
--('Paula Mendoza',      '2C3D4E5F6G7H8I9J0', 'Pasaporte', 'Empresarial', 'Débito',  '2010-05-21', 'Activa'),
--('Fernando Castro',    '2M3N4O5P6Q7R8S9T0', 'DNI',       'Personal',    'Crédito', '2009-08-03', 'Inactiva'),
--('Gabriela Ortiz',     '2W3X4Y5Z6A7B8C9D0', 'Cédula',    'Empresarial', 'Débito',  '2008-12-15', 'Activa'),
--('Fernando Castro',    '2G3H4I5J6K7L8M9N0', 'Pasaporte', 'Personal',    'Crédito', '2007-03-29', 'Activa'),
--('Valentina Romero',   '2Q3R4S5T6U7V8W9X0', 'DNI',       'Empresarial', 'Débito',  '2006-07-11', 'Inactiva'),
--('Santiago Vargas',    '2A3B4C5D6E7F8G9H0', 'Cédula',    'Personal',    'Crédito', '2005-11-23', 'Activa'),
--('Natalia Herrera',    '2K3L4M5N6O7P8Q9R0', 'Pasaporte', 'Empresarial', 'Débito',  '2004-04-05', 'Activa'),
('Sofía Sánchez',      '2E3F4G5H6I7J8K9L0', 'DNI',       'Personal',    'Crédito', '2015-11-18', 'Activa');

-- Gestion de identificadores duplicados
-- 2C3D4E5F6G7H8I9J0 aparece 2 veces:

-- Juan Pérez

-- Paula Mendoza

-- 2M3N4O5P6Q7R8S9T0 también aparece 2 veces:

-- María García

-- Fernando Castro

-- 2W3X4Y5Z6A7B8C9D0 también aparece 2 veces:

-- Carlos Rodríguez

-- Gabriela Ortiz

-- 2G3H4I5J6K7L8M9N0 también aparece 2 veces:

-- Ana Martínez

-- Fernando Castro

-- 2Q3R4S5T6U7V8W9X0 también aparece 2 veces:

-- Luis Hernández

-- Valentina Romero

-- 2A3B4C5D6E7F8G9H0 también aparece 2 veces:

-- Laura López

-- Santiago Vargas

-- 2K3L4M5N6O7P8Q9R0 también aparece 2 veces:

-- Pedro González

-- Natalia Herrera