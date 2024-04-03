import requests
import json

def getTipoMov():
    peticion = requests.get("http://localhost:5501/tipoMovActivos")
    data = peticion.json()
    return data