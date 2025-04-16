WITH transacciones_agrupadas AS (
    SELECT 
        t.IDENTIFICACION,
        t.CODIGO_CATEGORIA,
        COUNT(*) AS total_transacciones,
        MAX(t.FECHA_TRANSACCION) AS ultima_transaccion,
        SUM(CASE WHEN t.ESTADO = 'Aprobada' THEN 1 ELSE 0 END) AS transacciones_aprobadas,
        SUM(CASE WHEN t.ESTADO = 'Aprobada' THEN t.VALOR_COMPRA ELSE 0 END) AS valor_total_aprobado,
        ROW_NUMBER() OVER (PARTITION BY t.IDENTIFICACION ORDER BY COUNT(*) DESC) AS ranking
    FROM transaccion t
    -- Agregar filtro de ventana temporal aquí si se requiere
    -- WHERE t.FECHA_TRANSACCION BETWEEN '2020-01-01' AND '2023-12-31'
    GROUP BY t.IDENTIFICACION, t.CODIGO_CATEGORIA
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
WHERE 1=1
-- Agregar top n del ranking
AND ta.ranking <= 2
ORDER BY cl.NOMBRE, ta.ranking;
