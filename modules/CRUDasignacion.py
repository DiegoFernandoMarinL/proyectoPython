from tabulate import tabulate
import requests
import os
import json
import datetime
import modules.getActivos as gActivos
import modules.getAsignacion as gAsignacion
import modules.getPersonal as gPersona
import modules.getZonas as gZonas

def postAsignacion():
    os.system("cls")
    while True:
        try:
            nroItem = input("Ingrese el Nro Item: ")
            nroItem = int(nroItem)
            break
        except ValueError:
            print("El dato ingresado no es numero")

    newAsignacion = dict()        
    asignaciones = []
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            newAsignacion = val
       
    if newAsignacion:
        id = newAsignacion["id"]
        #validacion Nroasignacion
        nroAsignacion = gAsignacion.getNroAsignacion(nroItem)
        print("Nro asignacion: ",nroAsignacion)
        #validacion campo fecha
        fechaHora = datetime.datetime.now()   
        fechaHora = fechaHora.strftime("%Y-%m-%d %H:%M")
        print("Fecha/hora: ", fechaHora) 
        #validacion tipo de asignacion      
        print(f""" 
        Tipos de asignacion
        1. Persona
        2. Zona  
            """)
                
        while True:
            try:
                op = input("Tipo de asignacion: ")
                op = int(op)
                if op == 1:
                    tipoAsignacion = "Persona"
                    #validacion campo asignadoA
                    print()
                    print(tabulate(gPersona.getAllCedulaNombre(), headers="keys", tablefmt="github"))
                    print()
                    flag = 1
                    while flag == 1:
                        dato = input("Asignar a cedula/nit: ")
                        for val in gPersona.getAllData():
                            if val.get("nroId (CC, Nit)") == dato:
                                asignadoA = val.get("id")
                                flag = 0
                        if flag == 1:
                            print("Nro de cedula no encontrada")    
                    break
                elif op == 2:
                    tipoAsignacion = "Zona"
                    #validacion campo asignadoA
                    print()
                    print(tabulate(gZonas.getAllNombreZona(), headers="keys", tablefmt="github")) 
                    print()
                    flag = 1
                    while flag == 1:
                        dato = input("Asignar a nombre zona: ")
                        for val in gZonas.getAllData():
                            if val.get("nombreZona") == dato.title():
                                asignadoA = val.get("id")
                                flag = 0
                        if flag == 1:
                            print("Zona no encontrada")   
                    break
                else:
                    print("Opcion no valida")
            except ValueError:
                print("El dato ingresado no es numero")

        asignaciones.append({
            "NroAsignacion":nroAsignacion,
            "FechaAsignacion":fechaHora,
            "TipoAsignacion":tipoAsignacion,
            "AsignadoA":asignadoA

        })

        newAsignacion["asignaciones"] = asignaciones
        #estado cambia a asignado
        newAsignacion["idEstado"] = "1"

        peticion = requests.put(f"http://localhost:5501/activos/{id}", data=json.dumps(newAsignacion))
        if(peticion.status_code == 201 or peticion.status_code == 200):
            return("Activo asignado correctamente")
        else:
            return peticion.status_code
        
    else:
        return "Numero de item no encontrado"


    
            
                
            

