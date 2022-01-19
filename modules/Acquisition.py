# Import all the libraries
import requests
import pandas as pd


#make functions to download the data from the database 
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
    estaciones = pd.read_json("data/bicimad2.json", orient='records')
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
