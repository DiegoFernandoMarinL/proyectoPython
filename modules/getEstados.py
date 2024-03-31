import requests
import json

def getEstados():
    peticion = requests.get("http://192.168.1.39:5501/estados")
    data = peticion.json()
    return data