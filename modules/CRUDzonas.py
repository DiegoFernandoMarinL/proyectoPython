from tabulate import tabulate
import os
import re
import json
import requests
import modules.getZonas as gZonas

def postZonas():
    os.system("cls")
    newZona = dict()
    #valida campo nombre
    while True:
        try:
            dato = input("Nombre: ")
            data = gZonas.getNombreZona(dato)
            if data:
                print()
                print(tabulate(data, headers="keys", tablefmt="github"))
                print()
                raise Exception("La zona ya existe")
            else:
                newZona["nombreZona"] = dato.title()
                break
        except Exception as error:
            print(error)         
    #valida campo capacidad
    while True:
        try:
            dato = input("Total de capacidad: ")
            dato = int(dato)
            newZona["totalCapacidad"] = dato
            break
        except ValueError:
            print("El dato ingresado no es numero")

    peticion = requests.post("http://192.168.1.39:5501/zonas", data=json.dumps(newZona))
    if peticion.status_code == 201 or peticion.status_code == 200:
        return "Zona creada correctamente"
    else:
        return peticion.status_code

def updateZonas():
    os.system("cls")
    print()
    print(tabulate(gZonas.getAllData(), headers="keys", tablefmt="github"))
    print()
    #valida campo nombre
    newZona = dict()
    dato = input("Nombre: ")
    data = gZonas.getNombreZona(dato)
    for val in gZonas.getAllData():
        if val.get("nombreZona") == dato.title():
            newZona = val
            break
    if not newZona:
        return "Zona no encontrada"
    else:
        #valida campo capacidad
        while True:
            try:
                dato = input("Total de capacidad: ")
                dato = int(dato)
                newZona["totalCapacidad"] = dato
                break
            except ValueError:
                print("El dato ingresado no es numero")  
    
        id = newZona["id"]

        peticion = requests.put(f"http://192.168.1.39:5501/zonas/{id}", data=json.dumps(newZona))
        if peticion.status_code == 200 or peticion.status_code == 201:
            return "Zona actualizada correctamente"
        else:
            return peticion.status_code    

def findZonas():
    os.system("cls")
    dato = input("Nombre: ")
    data = gZonas.getNombreZona(dato)
    if data:
        print()
        print(tabulate(data, headers="keys", tablefmt="github"))
        print()
    else:
        return "Zona no encontrada"       