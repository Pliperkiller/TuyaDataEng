-- Ejemplos de uso fn top n preferencias consumo
--------------------------------------------------------------:
-- Con todos los parámetros:
SELECT * FROM fn_top_n_preferencias_consumo(3, '2020-01-01', '2023-12-31');

-- Solo con cantidad de categorías top (5):
SELECT * FROM fn_top_n_preferencias_consumo(5);

-- Solo con fecha de inicio:
SELECT * FROM fn_top_n_preferencias_consumo(2, '2021-01-01');

-- Solo con fecha de fin:
SELECT * FROM fn_top_n_preferencias_consumo(2, NULL, '2022-12-31');

--------------------------------------------------------------:
-- Ejemplos de uso sp specific n preferencias consumo
-- Con todos los parámetros:
SELECT * FROM fn_specific_n_preferencias_consumo(3, '2020-01-01', '2023-12-31');

-- Solo con cantidad de categorías top (2):
SELECT * FROM fn_specific_n_preferencias_consumo(2);

-- Solo con fecha de inicio:
SELECT * FROM fn_specific_n_preferencias_consumo(2, '2021-01-01');

-- Solo con fecha de fin:
SELECT * FROM fn_specific_n_preferencias_consumo(2, NULL, '2022-12-31');
