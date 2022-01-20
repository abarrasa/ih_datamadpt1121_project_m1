
from modules import Analysis as ana

df_resultado = ana.apply_distance()

#Define both options we want in the pipeline. "all_minimum"
def all_minimum():  
    return df_resultado.sort_values(by = "Distance", ascending = True).groupby('Place of interest')['Type of place','Place address','BiciMAD station', 'Station location','Distance'].nth(0).drop(["Distance"], axis = "columns").to_csv("All_Stations.csv", sep=";")

def minimum():
    df_minimo = df_resultado[df_resultado["Place of interest"] == input('Enter a place of interest: ')]
    minimum = df_minimo[df_minimo['Distance'] == df_minimo['Distance'].min()]
    minimum_mod = minimum[["Place of interest","Type of place","Place address","BiciMAD station","Station location","Distance"]]
    return minimum_mod.to_csv("Closer Station.csv", sep=";")