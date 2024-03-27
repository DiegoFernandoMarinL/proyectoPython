import requests
import json

def getEstados():
    peticion = requests.get("http://154.38.171.54:5501/estados")
    data = peticion.json()
    return data