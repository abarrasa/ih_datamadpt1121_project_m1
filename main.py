# Import all the libraries
import argparse
from modules import Wrangling as wa
from modules import Analysis as ana
from modules import Reporting as re
from modules import Acquisition as acq

if __name__ == '__main__':
    embassies_def = acq.embassies()
    stations_def = acq.stations()
    embassies_def = wa.mercator_emb()
    stations_def = wa.mercator_est()
    df_resultado = ana.apply_distance()

#To define the argparse function to make different options when getting the output
def argument_parser():
    parser = argparse.ArgumentParser(description='Emabassies and consulates')
    parser.add_argument('-op','--options', type=str, help= 'Inter "all" or "minimum" in order to print the BiciMAD stations')
    args=parser.parse_args()
    return args

def main(arguments):
    print('-- executing pipeline --')
    print('\n')
    if arguments.options == 'minimum':        
        print(re.minimum())
    elif arguments.options == 'all':
        print(re.all_minimum())

    print('\n')
    print('-- File exported --')

# Pipeline execution
if __name__ == '__main__':
    main(argument_parser())

