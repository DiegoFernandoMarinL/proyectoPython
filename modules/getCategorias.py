import requests
import json

def getCategorias():
    peticion = requests.get("http://localhost:5501/categoriasActivos")
    data = peticion.json()
    return data
