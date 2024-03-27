import requests
import json

def getCategorias():
    peticion = requests.get("http://154.38.171.54:5501/categoriaActivos")
    data = peticion.json()
    return data
