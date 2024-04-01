import requests
import json

def getEstados():
    peticion = requests.get("http://localhost:5501/estados")
    data = peticion.json()
    return data