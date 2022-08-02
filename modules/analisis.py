from os import rename
from unittest import result
import pandas as pd
import argparse
from wrangling_2 import diferencia_min, min_un_punto, pm_bm, un_valor 

bm_pm = pd.read_csv('pm_bm.csv')

# filter = ['Aparcamiento disuasorio Aviación Española']

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Application for arithmetic calculations' )
    help_message ='You have two options. Option 1:Registro completo. Option 2:Unico Registro'
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    print(type(argument_parser()))
    if argument_parser().function == 'pm_bm':
        result = pm_bm()
    elif argument_parser().function == 'diferencia_min':
        result = diferencia_min()
    elif argument_parser().function == 'min_un_punto':
        result = min_un_punto()
    elif argument_parser().function == 'un_valor':
        result = un_valor()
else:
    result = 'FATAL ERROR...you need to select the correct method'
print(f'The result is => {result}')
    
    
    
    #if argument_parser().function == 'Bici_Mad':
        #result = Bici_Mad()
    #elif argument_parser().function == 'disuasorios':
        #result = disuasorios()
    #elif argument_parser().function == 'publicos_municipales':
        #result = publicos_municipales()
    #elif argument_parser().function == 'publicos_residentes':
        #result = publicos_residentes()
    #elif argument_parser().function == 'parking_madrid':
        #result = parking_madrid()
    #elif argument_parser().function == 'separacion':
        #result = separacion()
    #elif argument_parser().function == 'limpieza':
        #result = limpieza
    #elif argument_parser().function == 'conversion':
        #result = conversion 
    #elif argument_parser().function == 'rename':
        #result = rename()
    #elif argument_parser().function == 'tabla_unica':
        #result = tabla_unica()
    #elif argument_parser().function == 'distance_meters':
        #result = distance_meters()
    #elif argument_parser().function == 'to_mercator':
        #result = to_mercator()
    #elif argument_parser().function == 'distancia_m':
        #result = distancia_m()
    #elif argument_parser().function == 'pm_bm':
        #result = pm_bm()
    #elif argument_parser().function == 'diferencia_min':
        #result = diferencia_min()
    #elif argument_parser().function == 'min_un_punto':
        #result = min_un_punto()
    #elif argument_parser().function == 'un_valor':
        #result = un_valor()
#else:
    #result = 'FATAL ERROR...you need to select the correct method'
#print(f'The result is => {result}')
