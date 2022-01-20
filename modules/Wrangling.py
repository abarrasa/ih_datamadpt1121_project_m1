
from modules import Acquisition as acq
from modules import geo_calculations as geo
import pandas as pd

embassies_def = acq.embassies()
stations_def = acq.stations()

def mercator_emb():
    embassies_def["mercator_start"] = embassies_def.apply(lambda x: geo.to_mercator(x['Latitude_start'],x['Longitude_start']),axis=1)
    return embassies_def

embassies_clean = mercator_emb()

def mercator_est():
    stations_def["mercator_finish"] = stations_def.apply(lambda x: geo.to_mercator(x['Latitude_finish'],x['Longitude_finish']),axis=1)
    return stations_def

stations_def = mercator_est()

def merge():
    df_resultado = pd.merge(embassies_def,stations_def, how="cross")
    return df_resultado

df_resultado = merge()