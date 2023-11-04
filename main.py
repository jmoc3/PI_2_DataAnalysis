import streamlit as st
from annotated_text import annotated_text

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Telecomunicaciones (DA - PI2)')
st.divider()
st.markdown('- En este apartado se hara un previo analisis de datasets suministrados por el [*ENACOM*](https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/) en APIS para el entendimiento del negocio y el desarrollo del mismo siguiendo la mision general de la empresa de telecomunicaciones: **Brindar acceso a internet**.  ')
st.markdown('- Para ello primero realizaremos un **EDA** completo entendiendo como se encuentran los datos crudos y que se puede hacer respecto a la limpieza de los mismos.')

key = 'FQ3taio22StSDU6EhW3BY5mjgPW0tIeKQnIYxP1X'
api = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/LISTA-DE-LOCAL-CON-CONEC/data.json/?auth_key={key}'
data = requests.get(api).json()

values = [item['fStr'] for item in data['result']['fArray']]
grouped_values = [values[i:i + 12] for i in range(0, len(values), 12)]

loc_w_conection = pd.DataFrame(grouped_values[1:],columns=grouped_values[0])


st.subheader('Sinopsis')
st.markdown('- Dentro de esta pagina trataremos con tres archivos  ')
st.markdown(':orange[Listado de localidades con conectividad a internet]')
st.dataframe(loc_w_conection)


api = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/VELOC-PROME-DE-BAJAD-DE/data.json/?auth_key={key}'
data = requests.get(api).json()

values = []
for i,x in enumerate(data['result']['fArray']):
  if x['fType']=='TEXT': values.append(x['fStr'])
  if x['fType']=='NUMBER': values.append(x['fNum'])

grouped_values = [values[i:i + 4] for i in range(0, len(values), 4)]

download_speed = pd.DataFrame(grouped_values[1:],columns=grouped_values[0])

st.markdown(':orange[Velocidad media de bajada de internet fijo por provincia]')
st.dataframe(download_speed)


st.markdown(':orange[Listado de licencias TIC otorgadas]')
api = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/LISTA-DE-LICEN-TIC-OTORG/data.json/?auth_key={key}'
data = requests.get(api).json()


values = [item['fStr'] for item in data['result']['fArray']]

grouped_values = [values[i:i+11] for i in range(0,len(values),11)]

TIC_lic = pd.DataFrame(grouped_values[1:],columns=grouped_values[0])

st.dataframe(TIC_lic)



st.subheader('EDA')
st.markdown('#### Listado de localidades con conectividad a internet')
st.markdown('##### Valores Faltantes')
annotated_text('Podemos ver que existen varios campos con valores que realmente ',("representan nulos","(--)"),' asi que vamos a reemplazar estos para detectar si algun registro no posee ningun valor relevante al analisis.')

loc_w_conection.replace('--',np.nan,inplace=True) ## Reemplazo de valores
st.code("loc_w_conection.replace('--',np.nan,inplace=True) ## Reemplazo de valores")
st.code("without_values = loc_w_conection.all() # Validamos valores")
st.code('without_values[without_values!=True] # Filtramos')
without_values = loc_w_conection.all() # Validamos valores
st.dataframe(without_values[without_values!=True])

st.markdown('Aparte de esos campos reemplazados por nulos, mas de la mitad de las columnas dentro de nuestro dataframe poseen valores de SI o NO que se pueden manejar mejor con ceros y unos.')

# Reemplazo de valores
loc_w_conection.replace('SI',1,inplace=True) 
loc_w_conection.replace(np.nan,0,inplace=True) 
# Casteamos flotantes
booleans = ['ADSL','Cablemódem','Dial Up','Fibra óptica','4G','3G','Telefonía Fija','Wireless','Satelital']
loc_w_conection[booleans] = loc_w_conection[booleans].astype(int)

code = '''# Reemplazo de valores
loc_w_conection.replace('SI',1,inplace=True) 
loc_w_conection.replace(np.nan,0,inplace=True) 
# Casteamos flotantes
booleans = ['ADSL','Cablemódem','Dial Up','Fibra óptica','4G','3G','Telefonía Fija','Wireless','Satelital']
loc_w_conection[booleans] = loc_w_conection[booleans].astype(int)
'''
st.code(code)

st.markdown('Por ultimo "Provincia" y "Localidad" son columnas con valores en mayuscula que por cuestion de comodidad capitalizaremos :')

loc_w_conection['Provincia'] = loc_w_conection['Provincia'].str.capitalize()
loc_w_conection['Localidad'] = loc_w_conection['Localidad'].str.capitalize()

code = '''
loc_w_conection['Provincia'] = loc_w_conection['Provincia'].str.capitalize()
loc_w_conection['Localidad'] = loc_w_conection['Localidad'].str.capitalize()
'''

st.code(code)
st.caption('Vistazo rapido')
st.dataframe(loc_w_conection)

con_features = loc_w_conection.drop(columns=['Provincia','Partido','Localidad']).sum().sort_values(ascending=False)
con_features['Others'] = 0

st.subheader('Representacion visual')

con_types = st.multiselect('Seleccione que tipos quiere mostrar: ',con_features.index,default=['Telefonía Fija','4G','Wireless','3G'])
df_types=con_features[con_features.index.isin(con_types)]
others = con_features[~con_features.index.isin(con_types)].sum()
df_types['Others'] = others

all_in = all(element in con_types for element in con_features.index)
if all_in:
  df_types.drop('Others',inplace=True)

colors = ['lightgray','lightyellow', 'moccasin', 'lightgreen', 'deepskyblue','sandybrown','salmon','lightpink','orchid']
plt.figure(figsize=(6,6))
plt.pie(df_types.sort_values(), labels=df_types.index,autopct='%1.1f%%',colors=colors)
plt.title('Tipos de conexiones en localidades argentinas')
st.pyplot(plt)
plt.close()

st.markdown('#### Velocidad media de bajada de internet fijo por provincia')
st.markdown('##### *Valores atipicos/extremos o outliers*')
st.markdown('Antes de empezar miremos si existen estos valores atipicos dentro de nuestra tabla "download_speed" :')

plt.boxplot(download_speed['Mbps (Media de bajada)']) # Se asigna el campo a graficar

# Se configura la grafica
plt.title('Velocidad media de bajada') 
plt.ylabel('Rango de valores')

st.pyplot(plt)
plt.close()

st.markdown('Ya sabiendo su existencia y una nocion de la cantidad que se encuentran dentro del dataset es importante hacer algo al respecto, para ello utilizaremos el rango intercuartil para determinar desde que valores se consideran estos campos outliers y filtrar el dataframe. ')

sorted_values = download_speed['Mbps (Media de bajada)'].sort_values() # Se ordenan
q1 = np.percentile(sorted_values,25) # Primer quartil
q3 = np.percentile(sorted_values,75) # Tercer quartil
RIC = q3 - q1 # Rango intercuartil
low = q1 - 1.5 * RIC # Outliers menores al grupo promedio
high = q3 + 1.5 * RIC # Outliers mayores al grupo promedio


code = '''
sorted_values = download_speed['Mbps (Media de bajada)'].sort_values() # Se ordenan
q1 = np.percentile(sorted_values,25) # Primer quartil
q3 = np.percentile(sorted_values,75) # Tercer quartil
RIC = q3 - q1 # Rango intercuartil
low = q1 - 1.5 * RIC # Outliers menores al grupo promedio
high = q3 + 1.5 * RIC # Outliers mayores al grupo promedio
'''

st.code(code)

st.caption('Registros atipicos')
st.dataframe(download_speed[(download_speed['Mbps (Media de bajada)']<low)|(download_speed['Mbps (Media de bajada)']>high)] 
)


download_speed = download_speed[(download_speed['Mbps (Media de bajada)']>low)&(download_speed['Mbps (Media de bajada)']<high)]

code = '''
# Filtramos Outliers
download_speed = download_speed[(download_speed['Mbps (Media de bajada)']>low)&(download_speed['Mbps (Media de bajada)']<high)]
'''
st.code(code)


mbps_per_anio = download_speed.groupby('Año').sum('Mbps (Media de bajada)')

plt.plot(mbps_per_anio)
plt.title("Velocidad de descarga a travez de los año")
plt.ylabel("Velocidad de descarga Total")
plt.xlabel("Año")

st.caption('Vistazo rapido')
st.pyplot(plt)
plt.close()

st.markdown('#### Listado de licencias TIC otorgadas')
st.markdown('Realmente en esta tabla no existe muchas cosas que cambiar aparte de algunos detalles que por lo general se hacen por cuestion de normalizacion como por ejemplo las fechas o los textos que queremos utilizar para unir tablas.')
st.dataframe(TIC_lic.sample(3)[['FECHA_RES','LOCALIDAD','PROVINCIA']])

st.markdown('Casteamos para un tipo de columna correspondiente a los datos que la componen:')
TIC_lic['FECHA_RES'] = pd.to_datetime(TIC_lic['FECHA_RES'],dayfirst=True).dt.date
st.code("TIC_lic['FECHA_RES'] = pd.to_datetime(TIC_lic['FECHA_RES'],dayfirst=True)")

st.markdown('Capitalizamos los textos:')
TIC_lic['LOCALIDAD'] = TIC_lic['LOCALIDAD'].str.capitalize()
TIC_lic['PROVINCIA'] = TIC_lic['PROVINCIA'].str.capitalize()
code = '''
TIC_lic['LOCALIDAD'] = TIC_lic['LOCALIDAD'].str.capitalize()
TIC_lic['PROVINCIA'] = TIC_lic['PROVINCIA'].str.capitalize()
'''
st.code(code)

st.markdown('Y por ultimo arreglamos un pequeño detalle: ')
TIC_lic['PROVINCIA'] = TIC_lic['PROVINCIA'].str.replace('Ciudad de buenos aires','Buenos aires')
st.code("TIC_lic['PROVINCIA'] = TIC_lic['PROVINCIA'].str.replace('Ciudad de buenos aires','Buenos aires')")

st.caption('Vistazo rapido')
st.dataframe(TIC_lic.sample(3))
grouped = TIC_lic.groupby('PROVINCIA')['DOMICILIO'].count().reset_index().sort_values('DOMICILIO')[-5:]
plt.barh(grouped['PROVINCIA'],width=grouped['DOMICILIO'],color='salmon')
plt.title("Provincias con mas licencias TIC")

st.pyplot(plt)
plt.close()

st.markdown("##### *Registros duplicados*")
st.code(f"Datos duplicados en 'Locaciones con internet': {loc_w_conection.duplicated().sum()}")
st.code(f"Datos duplicados en 'Velocidad de descarga': {download_speed.duplicated().sum()}")
st.code(f"Datos duplicados en 'Licencias TIC': {TIC_lic.duplicated().sum()}")
st.caption('Se resuelve:')
st.code('loc_w_conection.drop_duplicates(inplace=True) # Done')


