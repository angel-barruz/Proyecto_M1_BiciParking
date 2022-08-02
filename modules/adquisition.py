from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests

#Parkings Bici_Mad
# Nos conectamos a Base de Datos SQL y extraemos la tabla haciendo una Query
connection_string = 'mysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD'
engine = create_engine(connection_string)

inspector = inspect(engine)
inspector.get_table_names()
#type(inspector)

query = '''
SELECT *
FROM bicimad_stations
'''
df_bm = pd.read_sql_query(query, engine)
df_bm.to_csv('df_bm.csv')


###### API ayto info parkings:

#1. Aparcamientos municipales para residentes

response = requests.get('https://datos.madrid.es/egob/GET/catalogo/202584-0-aparcamientos-residentes.json')
print(type(response))
print(response)

content = response.content
content

headers = response.headers
headers

df_1 = response.json()

#2. Aparcamientos públicos municipales

response = requests.get('https://datos.madrid.es/egob/GET /catalogo/202625-0-aparcamientos-publicos.json')
print(type(response))
print(response)

content = response.content
content

df_2 = response.json()
df_2

#  3. Aparcamientos Públicos Municipales Disuasorios
response = requests.get('https://datos.madrid.es/egob/GET /catalogo/300531-0-aparcamientos-publicos.json')
print(type(response))
print(response)

content = response.content
content

headers = response.headers
headers

df_3 = response.json()
df_3