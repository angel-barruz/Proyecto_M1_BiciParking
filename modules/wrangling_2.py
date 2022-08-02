import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

# Data Frame Bici Mad
def Bici_Mad():
    df_bm = pd.read_csv('df_bm.csv')
    return df_bm

# Importamos tablas de Parking de la Comunidad de Madrid en formato CSV
# Aparcamientos Disuasorios
def disuasorios():
    df_1 = pd.read_csv('../csv/publicos-dis.csv', sep=';')
    df_1.columns
    df_1_n = df_1[['NOMBRE', 'LATITUD', 'LONGITUD']]
    df_1_n['Tipo'] = 'Disuasorio'
    return df_1_n

# Parkings públicos municipales
def publicos_municipales():
    df_2 = pd.read_csv('../csv/parkings.csv', sep=';')
    df_2.columns
    df_2_n = df_2[['NOMBRE', 'LATITUD', 'LONGITUD']]
    df_2_n['Tipo'] = 'Publicos Municipales'
    return df_2_n

# Parkings Públicos Residentes
def publicos_residentes():
    df_3 = pd.read_csv('../csv/residentes.csv', sep=';')
    df_3.columns
    df_3_n = df_3[['NOMBRE', 'LATITUD', 'LONGITUD']]
    df_3_n['Tipo'] = 'Residentes'
    return df_3_n

# Concat de las 3 Tablas de Parking Municipales en 1
def parking_madrid():
    parking_mad = pd.concat(['df_1_n', 'df_2_n', 'df_3_n'], axis=0)
    parking_mad['key'] = 0
    return parking_mad

# Separación de Latitud y Longitud de bici_mad
def separacion():
    Bici_Mad[['LONGITUD','LATITUD']]=Bici_Mad['geometry.coordinates'].str.split(',',expand=True)
    return Bici_Mad

# Limpieza de datos "[]"
def limpieza(LATITUD, LONGITUD):
    Bici_Mad['LATITUD'] = Bici_Mad['LATITUD'].str.replace("]","", regex=True)
    Bici_Mad['LONGITUD'] = Bici_Mad['LONGITUD'].str.replace("[","",regex=True)
    return Bici_Mad

# Convertir string a float
def conversion (LATITUD, LONGITUD):
    Bici_Mad['LATITUD'] = Bici_Mad['LATITUD'].astype(float)
    Bici_Mad['LONGITUD'] = Bici_Mad['LONGITUD'].astype(float)
    return Bici_Mad

# Renombramos, sacamos las tablas con las mismas columnas para poder hacer Merge y establecemos key ficticia para punto de unión
def rename():
    bici_Mad = Bici_Mad.columns
    bici_Mad = Bici_Mad.rename(columns = {'name':'NOMBRE'}, inplace = True)
    bici_Mad = Bici_Mad['NOMBRE', 'LATITUD', 'LONGITUD']
    bici_Mad['key'] = 0
    return bici_Mad

#Tabla única
def tabla_unica():
    Merge = rename.merge(rename, on='key', how='left')
    return Merge

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

# Distancia en Metros
def distancia_m():
    pm_bm['Diferencia'] = pm_bm.apply(lambda x: distance_meters(x['LATITUD_x'],
                                                            x['LONGITUD_x'],
                                                            x['LATITUD_y'],
                                                            x['LONGITUD_y'])
                                                            , axis=1)
    return pm_bm

# CSV del Dataframe  pm_bm
def pm_bm():
    pm_bm = pd.read_csv('../csv/pm_bm.csv')
    return pm_bm

# Calculamos el minimo de distancia
def diferencia_min():
    pm_bm.groupby(["Diferencia"]).min()
    return pm_bm

# Distancia mínima respecto a un punto
def min_un_punto():
    pm_bm = pm_bm.sort_values(by=['NOMBRE_x', 'Diferencia'])
    return pm_bm

# Filtro de una linea
def un_valor():
    pm_bm = pm_bm.sort_values(by=['NOMBRE_x', 'Diferencia'])
    return pm_bm
if pm_bm == "NOMBRE_x":
    print (input ("Introduzca destino"))