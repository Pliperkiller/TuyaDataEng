-- Retorna el listado de las rachas filtradas por la fecha y el valor maximo de racha
-- tambien retorna un unico valor por cliente, el de mayor racha y de fecha mas reciente
CREATE OR REPLACE FUNCTION FN_rachas_cliente_unico(n INT, fecha_base DATE)
RETURNS TABLE (
    identificacion TEXT,
    racha INT,
    fecha_fin DATE,
    nivel TEXT
) AS $$
BEGIN
    RETURN QUERY
    WITH rachas_filtradas AS (
        SELECT
            rn.identificacion,
            rn.nivel,
            rn.racha_maxima,
            rn.mes_fin_racha
        FROM fn_rachas_por_nivel_cliente(fecha_base) rn
        WHERE rn.racha_maxima >= n
    ),
    rachas_priorizadas AS (
        --Bandera por prioridad de racha_maxima y mes_fin_racha
        SELECT 
            rf.identificacion,
            rf.nivel,
            rf.racha_maxima,
            rf.mes_fin_racha,
            ROW_NUMBER() OVER (
                PARTITION BY rf.identificacion
                ORDER BY rf.racha_maxima DESC,--prioridad por racha_maxima
                         rf.mes_fin_racha DESC--prioridad por mes_fin_racha
            ) AS prioridad
        FROM rachas_filtradas rf
    )
    SELECT 
        rp.identificacion,
        rp.racha_maxima,
        rp.mes_fin_racha,
        rp.nivel
    FROM rachas_priorizadas rp
    WHERE rp.prioridad = 1
    ORDER BY rp.identificacion;
END;
$$ LANGUAGE plpgsql;

-- Ejemplo de uso:
SELECT * FROM FN_rachas_cliente_unico(3, '2023-12-31');

--drop function if exists FN_rachas_cliente_unico(n INT, fecha_base DATE);