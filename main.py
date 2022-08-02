from unittest import result
import pandas as pd
import argparse

df_final = pd.read_csv('../project_m1_new/df_final.csv')
print('Data loaded...')

# filter = ['Aparcamiento disuasorio Aviación Española']

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Application for arithmetic calculations' )
    help_message ='You have two options. Option 1:Registro completo. Option 2:Unico Registro'
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    print(type(argument_parser()))
    if argument_parser().function == 'todos':
        result = df_final
    elif argument_parser().function == 'uno':
        parking = input('Elija su parking: ')
        result =  df_final[df_final['Origen'] == parking]
    else:
        result = 'FATAL ERROR...you need to select the correct method'

print(f'The result is => {result}')
    