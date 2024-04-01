import requests
import json

def getTipoActivos():
    peticion = requests.get("http://localhost:5501/tipoActivos")
    data = peticion.json()
    return data