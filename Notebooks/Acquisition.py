#!/usr/bin/env python
# coding: utf-8

# In[91]:


import requests
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd 
import argparse


# In[92]:


def embajadas():
    response = requests.get('https://datos.madrid.es/egob/catalogo/201000-0-embajadas-consulados.json')
    results = response.json()
    embajadas = pd.json_normalize(results['@graph'])
    embajadas["Type of place"] = "Embajadas y consulados"
    embajadas["Dirección"] = embajadas["address.street-address"]
    embajadas["location.latitude"] = pd.to_numeric(embajadas["location.latitude"],errors = 'coerce')
    embajadas["location.longitude"] = pd.to_numeric(embajadas["location.longitude"],errors = 'coerce')
    embajadas_clean = embajadas[["title","Type of place", "Dirección","location.longitude","location.latitude"]]
    embajadas_clean = embajadas_clean.rename(columns={"title": "Place of interest", "Dirección": "Place address", "location.longitude": "Longitud_inicial", "location.latitude": "Latitud_inicial"}, errors="raise")
    return embajadas_clean

def estaciones():
    estaciones = pd.read_json("../data/bicimad2.json", orient='records')
    geometry_coordinates = estaciones["geometry_coordinates"].str.split(expand=True)
    geometry_coordinates.columns = ['LONGITUD', 'LATITUD']
    geometry_coordinates['LONGITUD'] = geometry_coordinates['LONGITUD'].str.replace("[","")
    geometry_coordinates['LONGITUD'] = geometry_coordinates['LONGITUD'].str.replace(",","")
    geometry_coordinates['LATITUD'] = geometry_coordinates['LATITUD'].str.replace("]","")
    estaciones = pd.concat([estaciones, geometry_coordinates], axis=1)
    estaciones["LONGITUD"] = pd.to_numeric(estaciones["LONGITUD"],errors = 'coerce')
    estaciones["LATITUD"] = pd.to_numeric(estaciones["LATITUD"],errors = 'coerce')
    estaciones_clean = estaciones[["name","address","LONGITUD","LATITUD"]]
    estaciones_clean = estaciones_clean.rename(columns={"name": "BiciMAD station", "address": "Station location", "LONGITUD": "Longitud_final", "LATITUD": "Latitud_final"})
    return estaciones_clean


# In[93]:


def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(mercator_start, mercator_finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    return mercator_start.distance(mercator_finish)
    


# In[94]:


#embajadas = pd.read_json('../data/embajadas.json')
#estaciones = pd.read_json('../data/estaciones.json')


# In[95]:


def mercator_emb():
    embajadas_clean["mercator_start"] = embajadas_clean.apply(lambda x: to_mercator(x['Longitud_inicial'], x['Latitud_inicial']), axis=1)
    return embajadas_clean

def mercator_est():
    estaciones_clean["mercator_finish"] = estaciones_clean.apply(lambda x: to_mercator(x["Latitud_final"], x["Longitud_final"]), axis=1)
    return estaciones_clean


# In[96]:


def merge():
    df_resultado = pd.merge(embajadas_clean,estaciones_clean, how='cross')
    return df_resultado


# In[97]:


def apply_distancia():
    df_resultado["Distancia"] = df_resultado.apply(lambda x: distance_meters(x["mercator_start"], x["mercator_finish"]), axis=1)
    return df_resultado


# In[98]:


def all_minimum():
    return df_resultado.sort_values(by = "Distancia", ascending = True).groupby('Place of interest')['Place address', 'Distancia','BiciMAD station', 'Station location'].nth(0).drop(["Distancia"], axis = "columns")


# In[99]:


estaciones_clean = estaciones()
embajadas_clean = embajadas()
embajadas_clean = mercator_emb()
estaciones_clean = mercator_est()
df_resultado = merge()
df_resultado = apply_distancia()
all_minimum()


# In[100]:


def minimum():
    df_minimo = df_resultado[df_resultado["Place of interest"] == input('Pon el lugar de interés: ')]
    df_minimum = df_minimo[df_minimo['Distancia'] == df_minimo['Distancia'].min()]
    minimum_mod = df_minimum[["Place of interest","Type of place", "Place address","BiciMAD station","Station location"]]
    return minimum_mod


# In[101]:


minimum()


# In[ ]:




