import requests
import json

def getMarcas():
    peticion = requests.get("http://localhost:5501/marcas")
    data = peticion.json()
    return data