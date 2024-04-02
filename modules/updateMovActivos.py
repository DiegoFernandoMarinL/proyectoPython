import os
import json
import requests
import modules.getActivos as gActivos
import modules.getHistorial as gHistorial

def retornoActivo():
    os.system("cls")
    while True:
        try:
            nroItem = input("Ingrese el Nro Item a retornar: ")
            nroItem = int(nroItem)
            break
        except ValueError:
            print("El dato ingresado no es numero") 

    updateActivo = dict()
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            updateActivo = val 
            id = updateActivo["id"]
            idEstado = val.get("idEstado")
            if idEstado == "1" or idEstado == "3": #asignado o reparacion
                updateActivo["idEstado"] = "0"
                historial = val.get("historialActivos")
                tipoMov = "4" #reasignado
                idResponsableMov = "Campuslands"
                historial = gHistorial.getHistorial(nroItem,historial,tipoMov,idResponsableMov)
                updateActivo["historialActivos"] = historial

                peticion = requests.put(f"http://localhost:5501/activos/{id}", data=json.dumps(updateActivo))
                if(peticion.status_code == 201 or peticion.status_code == 200):
                    return("Retorno activo correctamente")
                else:
                    return peticion.status_code
            elif idEstado == "2": #dado de baja
                return "Activo dañado no se puede retornar"
            elif idEstado == "0": #no asignado
                return "Activo no asignado no se puede retornar"
    return "Nro de item no encontrado"        

def bajaActivo():
    os.system("cls")
    while True:
        try:
            nroItem = input("Ingrese el Nro Item a retornar: ")
            nroItem = int(nroItem)
            break
        except ValueError:
            print("El dato ingresado no es numero") 

    updateActivo = dict()
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            updateActivo = val 
            id = updateActivo["id"]
            idEstado = val.get("idEstado")
            if idEstado == "0": #no asignado
                updateActivo["idEstado"] = "2"
                historial = val.get("historialActivos")
                tipoMov = "2" # dado de baja
                idResponsableMov = "Campuslands"
                historial = gHistorial.getHistorial(nroItem,historial,tipoMov,idResponsableMov)
                updateActivo["historialActivos"] = historial

                peticion = requests.put(f"http://localhost:5501/activos/{id}", data=json.dumps(updateActivo))
                if(peticion.status_code == 201 or peticion.status_code == 200):
                    return("Activo dado de baja correctamente")
                else:
                    return peticion.status_code
            elif idEstado == "2": #dado de baja
                return "El activo ya estaba dado de bajo"
            elif idEstado == "3": #reparacion
                return "Activo en reparacion o garantia no se puede dar de baja"
            elif idEstado == "1": #asignado
                return "Activo esta asignado no se puede dar de baja"

def cambiarAsignacionActivo():
    os.system("cls")
    while True:
        try:
            nroItem = input("Ingrese el Nro Item a retornar: ")
            nroItem = int(nroItem)
            break
        except ValueError:
            print("El dato ingresado no es numero") 

    updateActivo = dict()
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            updateActivo = val 
            id = updateActivo["id"]
            idEstado = val.get("idEstado")
            if idEstado == "0":
                updateActivo["idEstado"] = "2"
                historial = val.get("historialActivos")
                tipoMov = "2"
                idResponsableMov = "Campuslands"
                historial = gHistorial.getHistorial(nroItem,historial,tipoMov,idResponsableMov)
                updateActivo["historialActivos"] = historial

                peticion = requests.put(f"http://localhost:5501/activos/{id}", data=json.dumps(updateActivo))
                if(peticion.status_code == 201 or peticion.status_code == 200):
                    return("Activo dado de baja correctamente")
                else:
                    return peticion.status_code
            elif idEstado == "2":
                return "El activo ya estaba dado de bajo"
            elif idEstado == "3":
                return "Activo en reparacion o garantia no se puede dar de baja"
            elif idEstado == "1":
                return "Activo esta asignado no se puede dar de baja"
            
     
