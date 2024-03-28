import json
import requests

def getAllData():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    return data

def getEmail(email):
    mail = []
    for val in getAllData():
        if val.get("Email") == email:
            mail.append({
                "nombre":val.get("Nombre"),
                "email":val.get("Email")
            })
            return(mail)