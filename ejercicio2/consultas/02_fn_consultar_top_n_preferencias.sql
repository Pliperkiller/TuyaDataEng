CREATE OR REPLACE FUNCTION fn_top_n_preferencias_consumo(
    n INTEGER DEFAULT 2,
    fecha_inicio DATE DEFAULT NULL,
    fecha_fin DATE DEFAULT NULL
)
RETURNS TABLE(
    nombre_cliente VARCHAR,
    identificacion VARCHAR,
    tipo_documento VARCHAR,
    clasificacion VARCHAR,
    tipo_tarjeta VARCHAR,
    estado_tarjeta VARCHAR,
    nivel_preferencia BIGINT,
    categoria_preferida VARCHAR,
    total_transacciones BIGINT,
    transacciones_aprobadas BIGINT,
    valor_total_aprobado NUMERIC,
    fecha_ultima_transaccion TEXT,
    ciudad VARCHAR,
    departamento VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    WITH transacciones_agrupadas AS (
        SELECT 
            t.identificacion,
            t.codigo_categoria,
            COUNT(*) AS total_transacciones,
            MAX(t.fecha_transaccion) AS ultima_transaccion,
            SUM(CASE WHEN t.estado = 'Aprobada' THEN 1 ELSE 0 END) AS transacciones_aprobadas,
            SUM(CASE WHEN t.estado = 'Aprobada' THEN t.valor_compra ELSE 0 END) AS valor_total_aprobado,
            ROW_NUMBER() OVER (PARTITION BY t.identificacion ORDER BY COUNT(*) DESC) AS ranking
        FROM transaccion t
        WHERE (fecha_inicio IS NULL OR t.fecha_transaccion >= fecha_inicio)
          AND (fecha_fin IS NULL OR t.fecha_transaccion <= fecha_fin)
        GROUP BY t.identificacion, t.codigo_categoria
    )
    SELECT 
        cl.nombre AS nombre_cliente,
        cl.identificacion,
        cl.tipo_documento,
        cl.clasificacion,
        cl.tipo_tarjeta,
        cl.estado_tarjeta,
        ta.ranking AS nivel_preferencia,
        cat.nombre_categoria AS categoria_preferida,
        ta.total_transacciones,
        ta.transacciones_aprobadas,
        ta.valor_total_aprobado,
        TO_CHAR(ta.ultima_transaccion, 'DD/MM/YYYY') AS fecha_ultima_transaccion,
        cat.ciudad,
        cat.departamento
    FROM transacciones_agrupadas ta
    JOIN cliente cl ON ta.identificacion = cl.identificacion
    JOIN categoria cat ON ta.codigo_categoria = cat.codigo_categoria
    WHERE ta.ranking <= n
    ORDER BY cl.nombre, ta.ranking;
END;
$$ LANGUAGE plpgsql;

