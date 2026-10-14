# Reporte de Análisis de Datos - Pandas

`Zavala Medina Learning Pandas NC: 0150`

## 1. DataFrame Convertido
```text
        Parque      Pais  Visitantes_anio
0    Six Flags    México          3500000
1       Xcaret    México          2500000
2       Xel-Ha    México          1800000
3       Disney      EEUU         20000000
4    Universal      EEUU         10000000
5  Europa Park  Alemania          5500000
```

## 2.1 Primeras Filas (head)
```text
      Parque    Pais  Visitantes_anio
0  Six Flags  México          3500000
1     Xcaret  México          2500000
```

## 2.2 Últimas Filas (tail)
```text
        Parque      Pais  Visitantes_anio
4    Universal      EEUU         10000000
5  Europa Park  Alemania          5500000
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Parque               str
Pais                 str
Visitantes_anio    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   Parque           6 non-null      str  
 1   Pais             6 non-null      str  
 2   Visitantes_anio  6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Visitantes_anio'
```text
count    6.000000e+00
mean     7.216667e+06
std      6.921103e+06
min      1.800000e+06
25%      2.750000e+06
50%      4.500000e+06
75%      8.875000e+06
max      2.000000e+07
Name: Visitantes_anio, dtype: float64
```

## 4. Ordenar Ascendente por Visitantes_anio
```text
        Parque      Pais  Visitantes_anio
2       Xel-Ha    México          1800000
1       Xcaret    México          2500000
0    Six Flags    México          3500000
5  Europa Park  Alemania          5500000
4    Universal      EEUU         10000000
3       Disney      EEUU         20000000
```

## 5. Ordenar Descendente por Visitantes_anio
```text
        Parque      Pais  Visitantes_anio
3       Disney      EEUU         20000000
4    Universal      EEUU         10000000
5  Europa Park  Alemania          5500000
0    Six Flags    México          3500000
1       Xcaret    México          2500000
2       Xel-Ha    México          1800000
```

`Zavala Medina Learning Pandas NC: 0150`