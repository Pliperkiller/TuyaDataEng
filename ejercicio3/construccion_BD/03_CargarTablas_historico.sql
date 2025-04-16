-- Ejecutar desde la terminal de pgsql asegurarse de localizarse en la carpeta donde se encuentra rachas.csv

SET datestyle = 'MDY';
\copy historico_saldo (identificacion, corte_mes, saldo) FROM 'rachas.csv' WITH (FORMAT csv, HEADER true);
