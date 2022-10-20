# %% [markdown]
# # Python Data Visualization
# 
# ## Importar librerias y captura de datos de la web

# %%
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

# %% [markdown]
# ## Ordenar el df dejando solo los datos que se relacionen a PM10 (particulas en suspension)
# 
# Se extraer los datos mas importantes fecha y concentracion (pm10) con la función drop

# %%
df.drop(['Autoridad Ambiental', 'Nombre de la estaciÃ³n',
       'TecnologÃ­a', 'Latitud', 'Longitud', 'CÃ³digo del departamento',
       'Departamento', 'CÃ³digo del municipio', 'Nombre del municipio',
       'Tipo de estaciÃ³n', 'Tiempo de exposiciÃ³n', 
       'Nueva columna georreferenciada'], axis=1, inplace=True)

#df despues del drop
df.columns = ['fecha','variable','unidades','concentracion']

# %% [markdown]
# ## Columnas del DF

# %%
df.columns

# %% [markdown]
# ## Dimension del DF

# %%
df.shape

# %% [markdown]
# ## Se filtran los datos que contengan valores de PM10

# %%
dfFinal = df.drop(df[df['variable']!='PM10'].index)

# %%
dfFinal.drop(['variable','unidades'], axis=1, inplace=True)

# %%
dfFinal
dfFinal.shape

# %% [markdown]
# ## Finaliza la captura de datos y empieza la creacion de la visualizacion

# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
mpl.style.use('ggplot')#estilos de la representacion

#ordenamos el index
dfFinal.reset_index(inplace = True)
print(dfFinal)

#visualizacion de datos
dfFinal.plot(kind='scatter', x='fecha', y='concentracion', figsize=(10, 6), color='darkblue')

plt.title('Concentración de Particulas en suspensión durante el año 2014 en el Municipio de Segovia')
plt.xlabel('Fecha')
plt.xticks(rotation=90)
plt.ylabel('Concentración de PM10 en µg/m3')


