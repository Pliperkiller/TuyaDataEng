
# Prueba Técnica - Ingeniero de Datos (Conversion de datos)

---

# Prueba Técnica - Ejercicio 1: Conversión de Imágenes HTML a Base64

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
   git clone https://github.com/Pliperkiller/TuyaDataEng.git
   cd TuyaDataEng
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

---

## **Solución Implementada**

### **1. Estructura del Código**
El código se organiza en una clase principal llamada `Orquestador`, que coordina todo el proceso. Esta clase utiliza varias dependencias externas para realizar tareas específicas:
- **`IProcesadorImagenes`**: Interfaz para procesar imágenes (convertirlas a Base64).
- **`IBuscadorImagenes`**: Interfaz para buscar y leer imágenes desde URLs o rutas locales.
- **`IAnalizador`**: Interfaz para analizar el contenido HTML y extraer etiquetas `<img>`.
- **`BuscadorFactory`**: Fábrica para crear instancias de buscadores de imágenes según el tipo de URL.

---

### **2. Flujo de Trabajo**

#### **Paso 1: Procesar Archivos HTML**
El método `process_files` es el punto de entrada principal. Este método:
1. Recibe una lista de rutas a archivos o directorios.
2. Recopila todos los archivos HTML utilizando el método `_collect_html_files`.
3. Procesa cada archivo HTML individualmente llamando al método `_process_html_file`.

#### **Paso 2: Recopilar Archivos HTML**
El método `_collect_html_files`:
- Verifica si las rutas proporcionadas son archivos o directorios.
- Si es un directorio, busca recursivamente todos los archivos con extensiones `.html` o `.htm`.

#### **Paso 3: Procesar un Archivo HTML**
El método `_process_html_file` realiza las siguientes tareas:
1. **Leer el contenido del archivo HTML**:
   - Abre el archivo y lee su contenido como texto.
2. **Analizar el contenido HTML**:
   - Utiliza un analizador HTML (`parser`) para extraer todas las etiquetas `<img>` y sus atributos.
3. **Procesar cada imagen**:
   - Para cada etiqueta `<img>`:
     - Obtiene el atributo `src` (la URL o ruta de la imagen).
     - Convierte la URL relativa en una URL absoluta utilizando `_get_absolute_url`.
     - Descarga la imagen utilizando un buscador (`fetcher`) creado por `BuscadorFactory`.
     - Convierte la imagen a Base64 utilizando `IProcesadorImagenes`.
     - Reemplaza la URL original en el HTML con la versión Base64.
4. **Guardar el archivo HTML modificado**:
   - Escribe el contenido HTML modificado en un nuevo archivo con el sufijo `_base64`.

#### **Paso 4: Manejo de Errores**
- Si ocurre un error al procesar una imagen, se registra en la sección `fail` de los resultados.
- Si todas las imágenes se procesan correctamente, se registran en la sección `success`.

---

### **3. Conversión de Imágenes a Base64**
La conversión de imágenes a Base64 se realiza en los siguientes pasos:
1. **Descargar la imagen**:
   - Se utiliza un buscador (`IBuscadorImagenes`) para leer los datos binarios de la imagen desde una URL o ruta local.
2. **Determinar el tipo MIME**:
   - Se utiliza `IProcesadorImagenes` para identificar el formato de la imagen (por ejemplo, `image/jpeg` o `image/png`).
3. **Codificar en Base64**:
   - Los datos binarios de la imagen se convierten a una cadena Base64.
4. **Reemplazar en el HTML**:
   - La URL original de la imagen se reemplaza con la cadena Base64 en el atributo `src` de la etiqueta `<img>`.

---

### **4. Resultados**
El script genera dos tipos de resultados:
1. **HTML Modificado**:
   - Un nuevo archivo HTML con las imágenes incrustadas en formato Base64.
   - El archivo se guarda en la misma ubicación que el original, con el sufijo `_base64`.

2. **Resumen en JSON** (opcional):
   - Un archivo JSON que contiene un resumen del procesamiento:
     - **`success`**: Lista de imágenes procesadas exitosamente.
     - **`fail`**: Lista de imágenes que no pudieron procesarse, junto con el error correspondiente.

Ejemplo de archivo JSON:
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

### **5. Solución a Problemas Comunes**
- **Error: `relative path can't be expressed as a file URI`**:
  - Se solucionó utilizando `Path.resolve()` para convertir rutas relativas en absolutas antes de llamar a `Path.as_uri()`.

- **Error: `ModuleNotFoundError: No module named 'src'`**:
  - Se solucionó asegurando que el script se ejecuta desde la raíz del proyecto y configurando el `PYTHONPATH` correctamente.

---

### **6. Ejecución del Script**
El script se ejecuta desde la terminal con el siguiente comando:

```bash
python program.py <input> [--output-json <ruta_a_resultados.json>]
```

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

## Notas

- Asegúrate de que las rutas proporcionadas sean correctas y que los archivos HTML contengan imágenes válidas.
- Si encuentras el error `ModuleNotFoundError: No module named 'src'`, verifica que estés ejecutando el script desde la raíz del proyecto o configura el `PYTHONPATH` correctamente. En este contexto debes ingresar a la carpeta `ejercicio1` antes de ejecutar el program.py.

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
   - Estos scripts contienen las funciones almacenadas  necesarias para analizar las rachas de los clientes.
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

### 0. **Crecion de vista de niveles general**
   Esta vista produce un listado de los clientes, sus saldos y niveles en cada corte de mes y ademas la fecha de retiro si el cliente se encuentra en la tabla de retiros.

   **Ejemplo de uso**:
   ```sql
   SELECT * FROM vw_nivel_cliente;
   ```

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
