-- Ejemplo de uso de la función FN_rachas_por_nivel_cliente
SELECT * FROM fn_rachas_por_nivel_cliente('2023-12-31');

-- Ejemplo de uso de la función FN_rachas_cliente_unico
select * FROM fn_rachas_cliente_unico(3, '2024-12-01')