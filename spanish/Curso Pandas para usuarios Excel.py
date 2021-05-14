import pandas as pd
import numpy as np


# ----------------------------------------------
# Nota: Para ver los resultados de cualquier linea de código, escribe el código dentro de () en -> print()
# ----------------------------------------------

# mostrar todas las columnas
pd.set_option('display.max_columns', 20)

# leer achivo excel
df_excel = pd.read_csv('StudentsPerformance.csv')

# ----------------------------------------------
# Formulas: suma, promedio, max, min y contar
# ----------------------------------------------
# contar
df_excel['gender'].value_counts()
# formulas en columnas
# opcion 1
df_excel.describe()
# opcion 2
df_excel['math score'].sum()
df_excel['math score'].mean()
df_excel['math score'].max()
df_excel['math score'].min()
df_excel['math score'].count()
# formulas en filas
# opcion 1
df_excel['average'] = (df_excel['math score'] + df_excel['reading score'] + df_excel['writing score'])/3
# opcion 2
df_excel['average'] = df_excel.mean(axis=1)
# print(df_excel)
# ----------------------------------------------
# Condicionales: SI, SUMARSI, CONTARSI, PROMEDIOSI
# ----------------------------------------------
# Condicion SI
df_excel['pass/fail'] = np.where(df_excel['average'] > 70, 'Pass', 'Fail')

# Multiples condiciones SI
conditions = [
    (df_excel['average']>=90),
    (df_excel['average']>=80) & (df_excel['average']<90),
    (df_excel['average']>=70) & (df_excel['average']<80),
    (df_excel['average']>=60) & (df_excel['average']<70),
    (df_excel['average']>=50) & (df_excel['average']<60),
    (df_excel['average']<50),
]
values = ['A', 'B', 'C', 'D', 'E', 'F']
df_excel['grades'] = np.select(conditions, values)
# print(df_excel)

# SUMARSI, CONTARSI, PROMEDIOSI
# ejemplo: solo obtener el promedio para el genero femenino
df_female = df_excel[df_excel['gender'] == 'female']
df_female['average'] = df_female.mean(axis=1)
# print(df_female)
# ejemplo: solo obtener el promedio para el genero femenino y grupo B
df_sumifs = df_excel[(df_excel['gender'] == 'female') & (df_excel['race/ethnicity'] == 'group B')]
df_sumifs['sum'] = df_sumifs['math score'] + df_sumifs['reading score'] + df_sumifs['writing score']
# print(df_sumifs)

# ----------------------------------------------
# Dar formato/limpiar data
# ----------------------------------------------
# mayusculas, minusculas
df_excel['gender'] = df_excel['gender'].str.title()
# extraer strings de una columna
df_excel['group'] = df_excel['race/ethnicity'].str.extract(r'([A-Z])')
# identificar celdas vacias
print(df_excel[df_excel['gender'].isnull()])

# ----------------------------------------------
# BuscarV
# ----------------------------------------------
# ejemplo: juntar archivos mediante columna "id" que tienen en común
excel_1 = 'StudentsPerformance.csv'
excel_2 = 'LanguageScore.csv'

df_excel_1 = pd.read_csv(excel_1)
df_excel_2 = pd.read_csv(excel_2)

df_excel_1 = df_excel_1.reset_index()
df_excel_1 = df_excel_1.rename(columns={'index':'id'})

# juntar archivos excel/dataframes -> 2 opciones (merge, concat)
#merge
df_excel_3 = pd.merge(df_excel_1, df_excel_2, on='id', how='left')
df_excel_3['language score'].fillna('0', inplace=True)
#concat
df_excel_3 = pd.concat(
    [df_excel_1.set_index('id'), df_excel_2.set_index('id')], axis=1
)
df_excel_3['language score'].fillna('0', inplace=True)
print(df_excel_3)

# ----------------------------------------------
# Tabla pivote
# ----------------------------------------------
df_excel = pd.read_csv('StudentsPerformance.csv')
df_pivot = df_excel.pivot_table(index='race/ethnicity', values=['math score', 'writing score'],
                           aggfunc='max')
print(df_pivot)
# ----------------------------------------------
# Graficos con Matplotlib
# ----------------------------------------------

import matplotlib.pyplot as plt
# grafico de barras
df_plot = df_pivot.reset_index()
plt.bar(df_plot['race/ethnicity'], df_plot['math score'])
plt.show()