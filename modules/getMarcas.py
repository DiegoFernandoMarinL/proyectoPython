import requests
import json

def getMarcas():
    peticion = requests.get("http://192.168.1.39:5501/marcas")
    data = peticion.json()
    return data