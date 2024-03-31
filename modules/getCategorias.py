import requests
import json

def getCategorias():
    peticion = requests.get("http://192.168.1.39:5501/categoriasActivos")
    data = peticion.json()
    return data
