-- Ejecutar desde la terminal de pgsql asegurarse de localizarse en la carpeta donde se encuentra retiros.csv

SET datestyle = 'MDY';
\copy retiros (identificacion,fecha_retiro) FROM 'retiros.csv' WITH (FORMAT csv, HEADER true);
