import requests
import json

def getTipoActivos():
    peticion = requests.get("http://192.168.1.39:5501/tipoActivos")
    data = peticion.json()
    return data