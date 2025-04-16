-- Esta vista clasifica a los clientes según el nivel de saldo y maneja casos donde el cliente no aparece en un corte_mes.
-- Si el cliente no aparece en un corte_mes, se asigna el nivel N0,
-- corte_mes es posterior a la fecha de retiro el cliente ya no va a aparecer.

CREATE OR REPLACE VIEW vw_nivel_cliente AS
WITH 

db AS (
    SELECT 
        r.identificacion,
        r.corte_mes,
        COALESCE(r.saldo, 0) AS saldo,
        rt.fecha_retiro
    FROM historico_saldo r
    LEFT JOIN retiros rt ON r.identificacion = rt.identificacion
),
clasificados AS (
    SELECT 
        identificacion,
        corte_mes,
        saldo,
        fecha_retiro,
        CASE 
            WHEN saldo >= 0 AND saldo < 300000 THEN 'N0'
            WHEN saldo >= 300000 AND saldo < 1000000 THEN 'N1'
            WHEN saldo >= 1000000 AND saldo < 3000000 THEN 'N2'
            WHEN saldo >= 3000000 AND saldo < 5000000 THEN 'N3'
            WHEN saldo >= 5000000 THEN 'N4'
        END AS nivel
    FROM db
),

completados AS (
    SELECT 
        clientes.identificacion,
        cm.corte_mes,
        COALESCE(c.saldo, 0) AS saldo,
        clientes.fecha_retiro,
        CASE 
            WHEN c.identificacion IS NULL THEN 'N0'
            ELSE c.nivel
        END AS nivel
    FROM (
        SELECT DISTINCT corte_mes FROM historico_saldo
    ) cm
    CROSS JOIN (
        SELECT DISTINCT identificacion, fecha_retiro FROM db
    ) clientes
    LEFT JOIN clasificados c 
        ON c.identificacion = clientes.identificacion 
        AND c.corte_mes = cm.corte_mes
    WHERE cm.corte_mes <= COALESCE(clientes.fecha_retiro, cm.corte_mes)
)
SELECT * FROM completados;