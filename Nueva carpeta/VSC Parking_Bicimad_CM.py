#CSV Parking_CM

# Librerias
import pandas as pd
import requests
import json
import csv
import numpy
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
from shapely.geometry import Point
import geopandas as gpd

# Importamos tablas de Parking de la Comunidad de Madrid en formato CSV

# Aparcamientos Disuasorios
df_1 = pd.read_csv('../csv/publicos-dis.csv', sep=';')
df_1.columns
df_1_n = df_1[['NOMBRE', 'LATITUD', 'LONGITUD']]
df_1_n['Tipo'] = 'Disuasorio'
df_1_n.head(3)

# Parkings públicos municipales
df_2 = pd.read_csv('../csv/parkings.csv', sep=';')
df_2.columns
df_2_n = df_2[['NOMBRE', 'LATITUD', 'LONGITUD']]
df_2_n['Tipo'] = 'Publicos Municipales'
df_2_n.head(5)

# Parkings Públicos Residentes
df_3 = pd.read_csv('../csv/residentes.csv', sep=';')
df_3.columns
df_3_n = df_3[['NOMBRE', 'LATITUD', 'LONGITUD']]
df_3_n['Tipo'] = 'Residentes'
df_3_n.head(20)

# Concat de las 3 Tablas de Parking Municipales en 1
parking_mad = pd.concat([df_1_n, df_2_n, df_3_n], axis=0)
parking_mad['key'] = 0
parking_mad.head(3)

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
df_bm.head(3)

# Separación de Latitud y Longitud
df_bm[['LONGITUD','LATITUD']]=df_bm['geometry.coordinates'].str.split(',',expand=True)
df_bm.head (3)

# Limpieza de datos "[]"
df_bm['LATITUD'] = df_bm['LATITUD'].str.replace("]","", regex=True)
df_bm['LONGITUD'] = df_bm['LONGITUD'].str.replace("[","",regex=True)
df_bm.head(5)
print(df_bm.dtypes)

# Convertir string a float
df_bm['LATITUD'] = df_bm['LATITUD'].astype(float)
df_bm['LONGITUD'] = df_bm['LONGITUD'].astype(float)
df_bm.head(5)

print(df_bm.dtypes)

# Renombramos, sacamos las tablas con las mismas columnas para poder hacer Merge y establecemos key ficticia para punto de unión
bici_Mad = df_bm.columns
bici_Mad = df_bm.rename(columns = {'name':'NOMBRE'}, inplace = True)
bici_Mad = df_bm[['NOMBRE', 'LATITUD', 'LONGITUD']]
bici_Mad['key'] = 0
bici_Mad.head(3)

#Tabla única
pm_bm = parking_mad.merge(bici_Mad, on='key', how='left')
pm_bm.head(3)

#Cálculo Distancias
def distance_meters(lat_start, long_start, lat_finish, long_finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)

def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c


pm_bm['Diferencia'] = pm_bm.apply(lambda x: distance_meters(x['LATITUD_x'],
                                                            x['LONGITUD_x'],
                                                            x['LATITUD_y'],
                                                            x['LONGITUD_y'])
                                                            , axis=1)
pm_bm.head(5)

pm_bm.groupby(["Diferencia"]).min()

pm_bm.to_csv('pm_bm.csv')

# CSV del Dataframe  pm_bm
pm_bm = pd.read_csv('../csv/pm_bm.csv')
pm_bm

# Calculamos el minimo de distancia
pm_bm.groupby(["Diferencia"]).min()

# Distancia mínima respecto a un punto
pm_bm = pm_bm.sort_values(by=['NOMBRE_x', 'Diferencia'])
pm_bm.head(10)


