import numpy as np
import pandas as pd

import requests
from io import StringIO

#captura de datos de la web
orig_url='https://drive.google.com/file/d/1iYmo2Tw3ZHaOiSq2SdnSOnMXZTKwTJ9N/view?usp=sharing'#Url original

file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id #Direccion para capturar los datos segun ID
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df = pd.read_csv(csv_raw)

#print(df.head())
#df.iloc[:,[0,12,13,14]]
#print(df.columns)
#print(df.shape)
#print(df.columns)

df.drop(['Autoridad Ambiental', 'Nombre de la estaciÃ³n',
       'TecnologÃ­a', 'Latitud', 'Longitud', 'CÃ³digo del departamento',
       'Departamento', 'CÃ³digo del municipio', 'Nombre del municipio',
       'Tipo de estaciÃ³n', 'Tiempo de exposiciÃ³n', 
       'Nueva columna georreferenciada'], axis=1, inplace=True)

#df despues del drop
df.columns = ['fecha','variable','unidades','concentracion']
print(df.columns)
print(df.shape)

#Ordenar el df dejando solo los datos que se relacionen a PM10 (particulas en suspension)
dfFinal = df.drop(df[df['variable']!='PM10'].index)
#renombrar valor de unidades PENDIENTE

#ordenar indice de fila PENDIENTE

#extraer los datos mas importantes fecha y concentracion (pm10)
dfFinal.drop(['variable','unidades'], axis=1, inplace=True)

print(dfFinal)
print(dfFinal.shape)

#Finaliza la captura de datos y empieza la creacion de la visualizacion

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
mpl.style.use('ggplot')#estilos de la representacion

#ordenamos el index
dfFinal.reset_index(inplace = True)
print(dfFinal)

#visualizacion de datos
dfFinal.plot(kind='scatter', x='fecha', y='concentracion', figsize=(10, 6), color='darkblue')

plt.title('Concentración de Particulas en suspensión durante el año 2014 en el Municipio de Segovia')
plt.xlabel('Fecha')
plt.ylabel('Concentración de PM10 en µg/m3')

#Ordenar eje x formaeando las fechas solo con dia y mes PENDIENTE
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.show()

#trabajo con datos polyfit Ajuste polinomial de mínimos cuadrados.
#Ajuste un polinomio de grados grados a puntos (x, y) . Devuelve un 
#vector de coeficientes p que minimiza el error al cuadrado en el 
#orden deg , deg-1 , ... 0 .p(x) = p[0] * x**deg + ... + p[deg]

#cambiar topo de dato columna concentracion
dfFinal['concentracion'] = dfFinal['concentracion'].astype(str)
print(dfFinal.dtypes)

x = dfFinal['fecha']
y = dfFinal['concentracion']
fit = np.polyfit(x, y, deg=1)
fit