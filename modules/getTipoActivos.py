import requests
import json

def getTipoActivos():
    peticion = requests.get("http://154.38.171.54:5501/tipoActivos")
    data = peticion.json()
    return data