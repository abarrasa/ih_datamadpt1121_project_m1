import pandas as pd

from modules import Wrangling as wa
from modules import geo_calculations as geo

df_resultado = wa.merge()

# Here we create the column "Distance" and apply the "distance_meters" function 
def apply_distance():
    df_resultado["Distance"] = df_resultado.apply(lambda x: geo.distance_meters(x['mercator_start'],x['mercator_finish']),axis=1)
    return df_resultado
    
df_resultado = apply_distance()