import json
import requests

def getAllData():
    peticion = requests.get("http://192.168.1.39:5501/personas")
    data = peticion.json()
    return data

def getEmail(email):
    mail = []
    for val in getAllData():
        if val.get("Email") == email:
            mail.append({
                "Nombre":val.get("Nombre"),
                "Email":val.get("Email")
            })
            return(mail)

def getNroCedulaNit(cedula):
    CC = []
    for val in getAllData():
        if val.get("nroId (CC, Nit)") == cedula:
            CC.append({
                "Nro cedula/nit":val.get("nroId (CC, Nit)"),
                "Nombre":val.get("Nombre"),
                "Email":val.get("Email"),
                "Telefonos":val.get("Telefonos")
            })
            return(CC)        