# Proyecto Módulo 1

# 👶 Status
https://github.com/angel-barruz/project_m1_new

El código se canaliza vía Base de Datos SQL privada y CSV.
** Lo correcto debería haber sido canalaizar la Base de Datos SQL a través de la API de los Parkings Públicos de la Comunidad de Madrid, pero no ha sido posible porque las tablas en orígen de la API daban error.

🏃 Product Description

El objetivo del proyecto es localizar la estación Bici_Mad mas cercana, respecto a cada Parking de la Comunidad de Madirid (Municipales, Municipales - Residentes o Disuasorios)

El usuario final podrá consultar la información de dos formas:

    1. La relación de distancias mínimas entre los puntos de bici_Mad y parking_mad, lo podrá ver directamente en la tabla relacionada pm_bm
    2. Directamente en el pipe line, introduciendo el nombre del "Parking"

# 💻 Technology stack

El software está diseñado con dos Módulos + Main:

    Acquisition:  se guarda la Base de Datos MySQL Bici_Mad y los json convertidos de la API de los Parkings de la Comunidad de Madrid (** IMPORTANTE: Se sacan las tablas a partir de un CSV porque se tiene que limpiar los datos al dar error en formato json en la línea 322 de la tabla Parking Municipal) 

    Wrangling_2: el código elaborado en Jupyter Notebook, se pasa a funciones.

    Main: cargamos la tabla final de Parking_Mad y Bici_Mad para ejecutar argpararse y que el usuario pueda interactuar.

El lenguaje de programación utilizado es Python, versión 3.9
Las liberías utilizadas han sido:
   
    - Librería: pandas 
        import pandas as pd  
    - Librería: requests
        import requests 
    - Librería: json
        import json
    - Librería: csv
        import csv
    - Librería: numpy
        import numpy  
    - Librería: sqlalchemy. Biblioteca: create_engine e inspect 
        from sqlalchemy import create_engine 
        from sqlalchemy import inspect
    - Librería: shapely.geometry. Biblioteca: Point 
        from shapely.geometry import Point
    - Librería: geopandas 
        import geopandas as gpd 
    - Librería: argparse
        import argparse
    - Librería unittest. Biblioteca result
        from unittest import result
     

# 💥 Core 
El proyecto ha sido elaborado para obtener el dato de la estación de bicis mas cercano en el mínimo tiempo posible para el usuario.

    
# 🔧 Configuration

Existen 2 datasources para la conexion:

- MySQL Online Database: contiene la información de las estaciones Bici Mad
    Server:        SERVER_IP
    Database:      BiciMAD

- API REST:  Portal de datos abiertos del Ayuntamiento de Madrid.

La configuración para que corra el código es la siguiente:

    1. Creación de un entorno específico en Python denominado p_01
    2. Instalación en p_01, Python, versión 3.9
        2.1 Conda install ipykernel
    2. Instalación de librerías:
        2.1 Pandas: pip install pandas
        2.2 Numpy: pip install numpy
        2.3 Sqlalchemy: pip install sqlalchemy
        2.4 Shapely.geometry: pip install shapely 
        2.5 Geopandas: conda install geopandas

# 🙈 Usage

El código da un error en el método Groupby porque hay que correr el codigo desde el principio para que funcione.

# 📁 Folder structure
└── https://github.com/angel-barruz/project_m1_new
    ├── project_m1_new
        ├── README.md
        ├── VSC Parking_Bicimad_CM.py
        ├── project_m1_new
        ├── df_final.csv
        ├── pm_bm.csv
        └── .ipynb_checkpoints
                 └── API-checkpoint.ipynb
                 └── Distances-checkpoint.ipynb
                 └── Filtros-checkpoint.ipynb
                 └── Import DataBase-checkpoint.ipynb
                 └── Json-checkpoint.ipynb
# 💩 ToDo
Introduzca en la terminal de Visual Studio Code:

    1) (p_01) C:\ironhack\project_m1_new\modules>python main.py -f todos # Argaparse con toda la tabla
    2) (p_01) C:\ironhack\project_m1_new\modules>python main.py -f uno # Argarparse para introducir un Orígen.

# ℹ️ Further info
Para conectarse a la base de datos My SQL, Bici_Mad, será necesario hacerlo desde la IP de la escuela de Ironhack.
En caso contrario, será necesario facilitar la IP de cada usuario que quiera consultarla, al profesor para que habilite el permiso para poder concectarse.

# Resources

https://pandas.pydata.org/pandas-docs/stable/ # Documentactión de Pandas
https://docs.python.org/3/library/argparse.html # Argparse Documentation


# Aparcamientos públicos municipales
    https://datos.madrid.es/egob/GET /catalogo/202625-0-aparcamientos-publicos.json
# Aparcamientos públicos municipales para residentes
    https://datos.madrid.es/egob/GET /catalogo/202584-0-aparcamientos-residentes.json
# Aparcamientos disuasorios
    https://datos.madrid.es/egob/GET/GET /catalogo/300531-0-aparcamientos-publicos.json


# 💌 Contact info
Ángel Barruz Montalvo
Tel: 680 50 57 51
email: a.barruz@gmail.com
