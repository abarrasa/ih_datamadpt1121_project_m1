
from modules import Acquisition as acq
from modules import geo_calculations as geo
import pandas as pd

embajadas_clean = acq.embajadas()
estaciones_clean = acq.estaciones()

def mercator_emb():
    embajadas_clean["mercator_start"] = embajadas_clean.apply(lambda x: geo.to_mercator(x['Longitud_inicial'], x['Latitud_inicial']), axis=1)
    return embajadas_clean

embajadas_clean = mercator_emb()

def mercator_est():
    estaciones_clean["mercator_finish"] = estaciones_clean.apply(lambda x: geo.to_mercator(x["Latitud_final"], x["Longitud_final"]), axis=1)
    return estaciones_clean

estaciones_clean = mercator_est()

def merge():
    df_resultado = pd.merge(embajadas_clean,estaciones_clean, how='cross')
    return df_resultado

df_resultado = merge()