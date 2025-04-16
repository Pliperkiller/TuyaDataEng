-- Crea la tabla de clientes (DYM) --
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre                  VARCHAR(100),
    identificacion          VARCHAR(50),
    tipo_documento          VARCHAR(50),
    clasificacion           VARCHAR(50),
    tipo_tarjeta            VARCHAR(50),
    fecha_apertura_tarjeta  DATE,
    estado_tarjeta          VARCHAR(20)
);
CREATE INDEX idx_identificacion_cliente ON cliente (identificacion);
ALTER TABLE cliente ADD CONSTRAINT uq_cliente_identificacion UNIQUE (identificacion);


-- Crea la tabla de categorias (DYM) --
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    codigo_categoria  INTEGER,
    nombre_categoria  VARCHAR(50),
    ciudad           VARCHAR(50),
    departamento     VARCHAR(50)
);
CREATE INDEX idx_codigo_categoria ON categoria (codigo_categoria);
ALTER TABLE categoria ADD CONSTRAINT uq_categoria_codigo_categoria UNIQUE (codigo_categoria);

-- Crea la tabla de transacciones (FACT) --
CREATE TABLE transaccion (
    id SERIAL PRIMARY KEY,
    identificacion     VARCHAR(50),
    id_transaccion     INTEGER,
    fecha_transaccion  DATE,
    codigo_categoria   INTEGER,
    estado             VARCHAR(20),
    valor_compra       NUMERIC(10,2)
);
CREATE INDEX idx_identificacion_transaccion ON transaccion (identificacion);
CREATE INDEX idx_transaccion ON transaccion (id_transaccion);
CREATE INDEX idx_codigo_categoria_transaccion ON transaccion (codigo_categoria);

-- FK con cliente
ALTER TABLE transaccion
ADD CONSTRAINT fk_transaccion_cliente
FOREIGN KEY (identificacion)
REFERENCES cliente(identificacion);

-- FK con categoria
ALTER TABLE transaccion
ADD CONSTRAINT fk_transaccion_categoria
FOREIGN KEY (codigo_categoria)
REFERENCES categoria(codigo_categoria);


-- -- Limpieza de modelo creado
-- DROP INDEX idx_identificacion_transaccion;
-- DROP INDEX idx_transaccion;
-- DROP INDEX idx_codigo_categoria_transaccion;
-- DROP TABLE transaccion;

-- DROP INDEX idx_identificacion_cliente;
-- DROP TABLE cliente;

-- DROP INDEX idx_codigo_categoria;
-- DROP TABLE categoria;

