
from modules import Analysis as ana

df_resultado = ana.apply_distancia()

def all_minimum():
    return df_resultado.sort_values(by = "Distancia", ascending = True).groupby('Place of interest')['Place address', 'Distancia','BiciMAD station', 'Station location'].nth(0).drop(["Distancia"], axis = "columns")

def minimum():
    df_minimo = df_resultado[df_resultado["Place of interest"] == input('Pon el lugar de interés: ')]
    df_minimum = df_minimo[df_minimo['Distancia'] == df_minimo['Distancia'].min()]
    minimum_mod = df_minimum[["Place of interest","Type of place", "Place address","BiciMAD station","Station location"]]
    return minimum_mod

