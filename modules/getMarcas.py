import requests
import json

def getMarcas():
    peticion = requests.get("http://154.38.171.54:5501/marcas")
    data = peticion.json()
    return data