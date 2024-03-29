from tabulate import tabulate
import requests
import os
import modules.getActivos as gActivos

def postAsignacion():
    os.system("cls")
    while True:
        try:
            nroItem = input("Ingrese el Nro Item: ")
            nroItem = int(nroItem)
            break
        except ValueError:
            print("El dato ingresado no es numero")
    newActivo = dict()
    getItem = []
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            newActivo = val
            getItem.append({
                "id":val.get("id"),
                "NroItem":val.get("NroItem"),
                "NroSerial":val.get("NroSerial"),
                "CodigoCampus":val.get("CodCampus"),
                "Nombre":val.get("Nombre"),
                "idMarca":val.get("idMarca"),
                "idCategoria":val.get("idCategoria"),
                "idTipo":val.get("idTipo"),
                "ValorUnitario":val.get("ValorUnitario")
            })
            break
    if not getItem:
        return "No se encontro el Nro item"
    else:
        print()
        print(tabulate(getItem,headers="keys",tablefmt="github")) 
        input()

