# Import all the libraries
import argparse
from modules import Wrangling as wa
from modules import Analysis as ana
from modules import Reporting as re
from modules import Acquisition as acq

if __name__ == '__main__':
    embassies_clean = acq.embassies()
    stations_clean = acq.stations()
    embassies_clean = wa.mercator_emb()
    stations_clean = wa.mercator_est()
    df_resultado = ana.apply_distance()


def argument_parser():
    parser = argparse.ArgumentParser(description='Stations')
    parser.add_argument('-op','--options', type=str, help= 'Calculate the closest station from a point or several. “minumum” calculates the distance from an indicated monument. “all” calculates the nearest station from all monuments.')
    args=parser.parse_args()
    return args

def main(arguments):
    print('--//--- starting pipeline ---//--')
    print('\n')
    if arguments.options == 'minimum':        
        print(re.minimum())
    elif arguments.options == 'all':
        print(re.all_minimum())
    print('\n\n')
    #print(f'The result is ==> {result}')
    print('\n')
    print('--//--- closing pipeline ---//--')
    
# Pipeline execution
if __name__ == '__main__':
    main(argument_parser())
