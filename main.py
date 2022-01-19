# Import all the libraries
import argparse
from modules import Wrangling as wa
from modules import Analysis as ana
from modules import Reporting as re
from modules import Acquisition as acq

if __name__ == '__main__':
    embajadas_clean = acq.embajadas()
    estaciones_clean = acq.estaciones()
    embajadas_clean = wa.mercator_emb()
    estaciones_clean = wa.mercator_est()
    df_resultado = ana.apply_distancia()


def argument_parser():
    parser = argparse.ArgumentParser(description='Stations')
    parser.add_argument('-f','--function', type=str, help= 'Calculates the closest scaon from a point or several. “minumum” calculates the distance from an indicated monument. “all” calculates the nearest station from all monuments.')
    args=parser.parse_args()
    return args

def main(arguments):
    print('--//--- starting application ---//--')
    print('\n')
    if arguments.function == 'minimum':        
        print(re.minimum())
    elif arguments.function == 'all':
        print(re.all_minimum())
    print('\n\n')
    #print(f'The result is ==> {result}')
    print('\n')
    print('--//--- closing application ---//--')
    
# Pipeline execution
if __name__ == '__main__':
    main(argument_parser())
