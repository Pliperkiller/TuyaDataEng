--- Crear tabla DYM de retiros
CREATE TABLE retiros (
    id SERIAL PRIMARY KEY,
    identificacion VARCHAR(50),
    fecha_retiro DATE
);
CREATE INDEX idx_identificacion_retiros ON retiros (identificacion);

--- Crear tabla FACT de historicos
CREATE TABLE historico_saldo (
    id SERIAL PRIMARY KEY,
    identificacion VARCHAR(50),
    corte_mes DATE,
    saldo NUMERIC(12,2)
);
CREATE INDEX idx_identificacion_historico_saldo ON historico_saldo (identificacion);


-- -- Limpieza de modelo creado
-- DROP INDEX idx_identificacion_historico_saldo;
-- DROP TABLE historico_saldo;

-- DROP INDEX idx_identificacion_retiros;
-- DROP TABLE retiros;