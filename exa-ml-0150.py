import sys
import os
import io
import pandas as pd
print("Zavala Medina Learning Pandas NC: 0150")

# Permitir importar dicc-0150.py desde la subcarpeta hermana
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos_de_entrada_ml_0150')))
import dicc_0150

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Zavala Medina Learning Pandas NC: 0150"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0150.datos_parques)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Visitantes_anio)
registrar("3. Estadísticas Generales de la Columna 'Visitantes_anio'", df['Visitantes_anio'].describe())

# 4. Ordenar Ascendente por Visitantes_anio
df_asc_visitantes = df.sort_values(by="Visitantes_anio", ascending=True)
registrar("4. Ordenar Ascendente por Visitantes_anio", df_asc_visitantes)

# 5. Ordenar Descendente por Visitantes_anio
df_desc_visitantes = df.sort_values(by="Visitantes_anio", ascending=False)
registrar("5. Ordenar Descendente por Visitantes_anio", df_desc_visitantes)

# 6. Guardar el archivo resultados-ml-0150.md dentro de resultados-0150
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0150'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0150.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"Archivo generado correctamente en: {ruta_archivo_md}")
print("Zavala Medina NC: 0150")