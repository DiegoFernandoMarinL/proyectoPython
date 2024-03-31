import json
import requests

def getAllData():
    peticion = requests.get("http://192.168.1.39:5501/zonas")
    data = peticion.json()
    return data

def getNombreZona(nombre):
    name = []
    for val in getAllData():
        if val.get("nombreZona") == nombre.title():
            name.append({
                "Nombre":val.get("nombreZona"),
                "Capacidad":val.get("totalCapacidad")    
            })
            return name
