# Import all the libraries
import requests
import pandas as pd

#make functions to download the data from the database 
def embassies():
    response = requests.get('https://datos.madrid.es/egob/catalogo/201000-0-embajadas-consulados.json')
    resultado = response.json()
    embassies = pd.json_normalize(resultado['@graph'])
    embassies["Type of place"]= "Embajadas y Consulados"
    embassies = embassies.rename(columns={"title": "Place of interest", "address.street-address": "Place address", "location.longitude": "Longitude_start", "location.latitude": "Latitude_start"}, errors="raise")
    embassies_def = embassies[["Place of interest","Type of place","Place address","Longitude_start","Latitude_start"]]
    embassies_def['Latatitude_start'] = pd.to_numeric(embassies_def['Latitude_start'],errors = 'coerce')
    embassies_def['Longitude_start'] = pd.to_numeric(embassies_def['Longitude_start'],errors = 'coerce')
    return embassies_def

def stations():
    stations = pd.read_json("data/bicimad.json", orient='records')
    geometry_coordinates = stations["geometry_coordinates"].str.split(expand=True)
    geometry_coordinates.columns = ['LONGITUD', 'LATITUD']
    geometry_coordinates['LONGITUD'] = geometry_coordinates['LONGITUD'].str.replace("[","")
    geometry_coordinates['LONGITUD'] = geometry_coordinates['LONGITUD'].str.replace(",","")
    geometry_coordinates['LATITUD'] = geometry_coordinates['LATITUD'].str.replace("]","")
    stations = pd.concat([stations, geometry_coordinates], axis=1)
    stations_def = stations.rename(columns={"name": "BiciMAD station", "address": "Station location", "LONGITUD": "Longitude_finish", "LATITUD": "Latitude_finish"}, errors="raise")
    stations_def = stations_def[["BiciMAD station","Station location","Longitude_finish","Latitude_finish"]]
    stations_def['Latitude_finish'] = pd.to_numeric(stations_def['Latitude_finish'],errors = 'coerce')
    stations_def['Longitude_finish'] = pd.to_numeric(stations_def['Longitude_finish'],errors = 'coerce')
    return stations_def
