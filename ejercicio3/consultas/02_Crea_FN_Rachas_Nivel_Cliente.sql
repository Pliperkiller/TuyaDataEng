-- Procedimiento almacenado para calcular rachas consecutivas de niveles antes de una fecha de corte
CREATE OR REPLACE FUNCTION fn_rachas_por_nivel_cliente(fecha_base DATE)
RETURNS TABLE (
    identificacion TEXT,
    nivel TEXT,
    racha_maxima INT,
    mes_fin_racha DATE
) AS $$
BEGIN
    RETURN QUERY
    WITH datos_filtrados AS (
        SELECT 
            vw.identificacion,
            vw.corte_mes,
            vw.nivel
        FROM vw_nivel_cliente vw
        WHERE vw.corte_mes < fecha_base
    ),
    con_grupos AS (
        -- Bandera para continuidad en nivel
        SELECT 
            df.identificacion,
            df.corte_mes,
            df.nivel,
            CASE 
                WHEN df.nivel = LAG(df.nivel) OVER (PARTITION BY df.identificacion ORDER BY df.corte_mes) THEN 0
                ELSE 1
            END AS cambio_nivel
        FROM datos_filtrados df
    ),
    grupos AS (
        -- Contador de banderas
        SELECT 
            cg.identificacion,
            cg.corte_mes,
            cg.nivel,
            SUM(cg.cambio_nivel) OVER (PARTITION BY cg.identificacion ORDER BY cg.corte_mes) AS grupo_racha
        FROM con_grupos cg
    ),
    rachas AS (
        SELECT 
            g.identificacion,
            g.nivel,
            g.grupo_racha,
            COUNT(*) AS racha_consecutiva,
            MAX(g.corte_mes) AS mes_fin_racha
        FROM grupos g
        GROUP BY g.identificacion, g.nivel, g.grupo_racha
    )
    SELECT 
        r.identificacion::TEXT,
        r.nivel::TEXT,
        MAX(r.racha_consecutiva)::INT AS racha_maxima,
        MAX(r.mes_fin_racha)::DATE AS mes_fin_racha
    FROM rachas r
    GROUP BY r.identificacion, r.nivel
    ORDER BY r.identificacion, r.nivel;
END;
$$ LANGUAGE plpgsql;
-- Ejemplo de uso:
SELECT * FROM fn_rachas_por_nivel_cliente('2023-12-31');