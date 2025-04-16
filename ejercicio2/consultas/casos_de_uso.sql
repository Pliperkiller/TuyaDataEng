-- Ejemplos de uso sp top n preferencias consumo
--------------------------------------------------------------:
-- Con todos los parámetros:
SELECT * FROM sp_top_n_preferencias_consumo(3, '2020-01-01', '2023-12-31');

-- Solo con cantidad de categorías top (5):
SELECT * FROM sp_top_n_preferencias_consumo(5);

-- Solo con fecha de inicio:
SELECT * FROM sp_top_n_preferencias_consumo(2, '2021-01-01');

-- Solo con fecha de fin:
SELECT * FROM sp_top_n_preferencias_consumo(2, NULL, '2022-12-31');

--------------------------------------------------------------:
-- Ejemplos de uso sp specific n preferencias consumo
-- Con todos los parámetros:
SELECT * FROM sp_specific_n_preferencias_consumo(3, '2020-01-01', '2023-12-31');

-- Solo con cantidad de categorías top (2):
SELECT * FROM sp_specific_n_preferencias_consumo(2);

-- Solo con fecha de inicio:
SELECT * FROM sp_specific_n_preferencias_consumo(2, '2021-01-01');

-- Solo con fecha de fin:
SELECT * FROM sp_specific_n_preferencias_consumo(2, NULL, '2022-12-31');
