
from modules import Analysis as ana
from fuzzywuzzy import process
from modules import Wrangling as wa

embassies_def=wa.mercator_emb()
df_resultado = ana.apply_distance()

#Define both functions to obtain two option when executing the pipeline. 
#Obtain the nearest BiciMAD station to each of the embassies and consulates from Madrid
def all_minimum():  
    return df_resultado.sort_values(by = "Distance", ascending = True).groupby('Place of interest')['Type of place','Place address','BiciMAD station', 'Station location','Distance'].nth(0).drop(["Distance"], axis = "columns").to_csv("All_Stations.csv", sep=";")

#Obtain the nearest BiciMAD station to an specific output.
def minimum():
    ok= list(embassies_def["Place of interest"].unique())
    user = input('Enter a place of interest: ')
    aprox=process.extractOne(user, ok, score_cutoff=80)
    df_minimo = df_resultado[df_resultado["Place of interest"] == aprox[0]]
    minimum = df_minimo[df_minimo['Distance'] == df_minimo['Distance'].min()]
    minimum_mod = minimum[["Place of interest","Type of place","Place address","BiciMAD station","Station location"]]
    return minimum_mod.to_csv("Closer Station.csv", sep=";")
