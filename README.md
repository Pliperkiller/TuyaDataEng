
# Prueba Técnica - Conversión de Imágenes HTML a Base64

Este proyecto es parte de una prueba técnica que consta de tres ejercicios. El primer ejercicio se encarga de procesar archivos HTML, localizar las imágenes referenciadas en ellos y convertirlas al formato Base64. El resultado es un archivo HTML modificado donde las imágenes se incrustan directamente en el código.

---

## Prueba Técnica - Ejercicio 1: Conversión de Imágenes HTML a Base64

### Descripción
El objetivo de este ejercicio es procesar archivos HTML y convertir las imágenes referenciadas en formato binario (Base64). Esto es útil para incrustar imágenes directamente en el HTML, eliminando la necesidad de referencias externas.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.7 o superior**
- **Pip** (administrador de paquetes de Python)

---

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crea un entorno virtual para el proyecto:
   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

### Comando para ejecutar el script

El script principal se encuentra en el archivo 

program.py

. Puedes ejecutarlo con el siguiente comando:

```bash
python program.py <input> [--output-json <ruta_a_resultados.json>]
```

#### Argumentos:
- `<input>`: Ruta al archivo HTML o directorio que contiene los archivos HTML a procesar.
- `--output-json`: (Opcional) Ruta donde se guardarán los resultados en formato JSON.

#### Ejemplo 1: Procesar un archivo HTML
```bash
python program.py ejemplo.html
```

#### Ejemplo 2: Procesar un directorio completo
```bash
python program.py ./html_files/
```

#### Ejemplo 3: Guardar los resultados en un archivo JSON
```bash
python program.py ejemplo.html --output-json resultados.json
```

---

## Resultados

El script genera un archivo HTML modificado con las imágenes convertidas a Base64. Además, si se especifica el argumento `--output-json`, se genera un archivo JSON con el resumen del procesamiento.

### Ejemplo de archivo JSON:
```json
{
  "success": {
    "ejemplo.html": [
      "https://example.com/image1.jpg",
      "https://example.com/image2.png"
    ]
  },
  "fail": {
    "otro.html": [
      {
        "src": "https://example.com/image3.jpg",
        "error": "No se pudo descargar la imagen"
      }
    ]
  }
}
```

---

## Notas

- Asegúrate de que las rutas proporcionadas sean correctas y que los archivos HTML contengan imágenes válidas.
- Si encuentras el error `ModuleNotFoundError: No module named 'src'`, verifica que estés ejecutando el script desde la raíz del proyecto o configura el `PYTHONPATH` correctamente.

---

# Prueba Técnica - Ejercicio 2: Funciones para Preferencias de Consumo

Este ejercicio consta de la implementación de funciones (stored procedures) que cumplen con dos propósitos principales:

1. **Crear un Top N de preferencias de consumo**: Genera un ranking de las categorías más preferidas por los clientes, basado en sus transacciones.
2. **Buscar un N específico**: Permite consultar información detallada sobre un cliente o categoría específica, según los parámetros proporcionados.

---

## Propósito

El objetivo de este ejercicio es analizar las preferencias de consumo de los clientes a partir de sus transacciones, clasificarlas y generar reportes que permitan identificar patrones de comportamiento.

---

## Orden de Ejecución

Para garantizar que las funciones y consultas funcionen correctamente, sigue este orden de ejecución:

1. **Scripts de Construcción de la Base de Datos**:
   - Estos scripts crean las tablas, índices y datos iniciales necesarios para el funcionamiento de las consultas.
   - Se encuentran en la carpeta `construccion_BD`.
   - **Ejemplo**:
     ```sql
     -- Ejecutar en orden numérico
     01_CrearTablas.sql
     02_CargarTAblas_Categorias.sql
     ...

     ```

2. **Scripts de Consultas**:
   - Estos scripts contienen las funciones y consultas necesarias para generar el Top N de preferencias y buscar un N específico.
   - Se encuentran en la carpeta `consultas`.
   - **Ejemplo**:
     ```sql
     -- Ejecutar en orden numérico
     01_PlantillaConsulta.sql
     02_fn_consultar_top_n_preferencias.sql
     03_fn_consulta_specific_n_preferencias.sql
     ```

3. **Validación**:
   - Una vez ejecutados los scripts, utiliza las consultas disponibles en los casos de uso para validar los resultados.

---

## Uso de las Funciones

### 1. **Top N Preferencias**
   Esta función genera un ranking de las categorías más preferidas por los clientes, basado en el número de transacciones realizadas.

   **Ejemplo de uso**:
   ```sql
   SELECT * FROM fn_top_n_preferencias(5);
   ```
   - **Parámetro**: `n` (opcional, por defecto 5) indica el número de categorías a incluir en el ranking.

### 2. **Buscar un N Específico**
   Esta función permite consultar información detallada sobre un cliente o categoría específica.

   **Ejemplo de uso**:
   ```sql
   SELECT * FROM fn_specific_n_preferencias_consumo(2, '2023-01-01', '2023-12-31');
   ```
   - **Parámetros**:
     - `n`: Número específico de preferencias a buscar.
     - `fecha_inicio` (opcional): Fecha inicial del rango de búsqueda.
     - `fecha_fin` (opcional): Fecha final del rango de búsqueda.

---

## Validación

Una vez ejecutados los scripts, puedes validar los resultados utilizando las consultas de los casos de uso proporcionados. Estas consultas están diseñadas para verificar que las funciones devuelvan los resultados esperados.

---

## Notas

- Asegúrate de ejecutar los scripts en el orden numérico indicado para evitar errores de dependencias.
- Si encuentras algún problema, verifica que las tablas y datos iniciales se hayan creado correctamente en la base de datos.
- Las funciones están diseñadas para ser flexibles y aceptar parámetros opcionales, pero asegúrate de proporcionar los valores necesarios según el caso de uso.

---

# Prueba Técnica - Ejercicio 3: Análisis de Rachas de Clientes

Este ejercicio se centra en analizar las rachas de comportamiento de los clientes, clasificándolos según su nivel y duración de las rachas. La solución se implementó utilizando **funciones almacenadas (stored procedures)** en PostgreSQL.

---

## Propósito

El objetivo de este ejercicio es identificar y analizar las rachas de comportamiento de los clientes, priorizando aquellas más largas y recientes. Esto permite obtener información valiosa sobre el comportamiento de los clientes en diferentes niveles.

---

## Orden de Ejecución

Para garantizar que las funciones y consultas funcionen correctamente, sigue este orden de ejecución:

1. **Cargue de Datos**:
   - Los datos necesarios para este ejercicio se cargaron en las tablas de la base de datos mediante archivos CSV.
   - El cargue se realizó utilizando comandos en la terminal de PostgreSQL, como el siguiente:
     ```sql
     \COPY nombre_tabla FROM 'ruta_del_archivo.csv' DELIMITER ',' CSV HEADER;
     ```
   - Asegúrate de que los archivos CSV estén correctamente formateados y que las tablas correspondientes ya existan en la base de datos.

2. **Scripts de Construcción de la Base de Datos**:
   - Estos scripts crean las tablas necesarias para almacenar los datos de las rachas y transacciones.
   - Se encuentran en la carpeta `construccion_BD`.
   - **Ejemplo**:
     ```sql
     -- Ejecutar en orden numérico
     01_CrearTablas.sql
     02_cargarTablas_retiros.sql
     ...

     ```

3. **Scripts de Consultas**:
   - Estos scripts contienen las funciones almacenadas necesarias para analizar las rachas de los clientes.
   - Se encuentran en la carpeta `consultas`.
   - **Ejemplo**:
     ```sql
     -- Ejecutar en orden numérico
     01_Crea_VW_Clasificacion_Cliente.sql
     02_Crea_FN_Rachas_Nivel_Cliente.sql
     03_Crea_FN_Rachas_Cliente_Unico.sql
     ```

4. **Validación**:
   - Una vez ejecutados los scripts, utiliza las consultas disponibles en los casos de uso para validar los resultados.

---

## Uso de las Funciones

### 1. **Cálculo de Rachas**
   Esta función calcula las rachas de comportamiento de los clientes, clasificándolas por nivel y duración.

   **Ejemplo de uso**:
   ```sql
   SELECT * FROM fn_rachas_por_nivel_cliente('2023-12-31');
   ```
   - **Parámetro**:
     - `fecha_base`: Fecha límite para calcular las rachas.

### 2. **Rachas de Cliente Único**
   Esta función devuelve la racha más larga y reciente para cada cliente.

   **Ejemplo de uso**:
   ```sql
   SELECT * FROM fn_rachas_cliente_unico(3, '2023-12-31');
   ```
   - **Parámetros**:
     - `n`: Número mínimo de meses consecutivos para considerar una racha.
     - `fecha_base`: Fecha límite para calcular las rachas.

---

## Validación

Una vez ejecutados los scripts, puedes validar los resultados utilizando las consultas de los casos de uso proporcionados. Estas consultas están diseñadas para verificar que las funciones devuelvan los resultados esperados.

---

## Notas

- Asegúrate de cargar los datos correctamente desde los archivos CSV antes de ejecutar los scripts.
- Ejecuta los scripts en el orden numérico indicado para evitar errores de dependencias.
- Las funciones almacenadas están diseñadas para ser flexibles y aceptar parámetros opcionales, pero asegúrate de proporcionar los valores necesarios según el caso de uso.

---

## Licencia

Este proyecto es parte de una prueba técnica y no tiene una licencia específica.
