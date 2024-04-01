from tabulate import tabulate
import requests
import os
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
            
    asignaciones = []
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            newAsignacion = val

    #validacion Nroasignacion
    nroAsignacion = gAsignacion.getNroAsignacion(nroItem)
    print("Nro asignacion: ",nroAsignacion)
    asignaciones.append({"NroAsignacion":nroAsignacion})
    #validacion campo fecha
    fechaHora = datetime.datetime.now()        
    print("Fecha/hora: ",fechaHora.strftime("%Y-%m-%d %H:%M")) 
    asignaciones.append({"FechaAsignacion":fechaHora.strftime("%Y-%m-%d %H:%M")})
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
                asignaciones.append({"TipoAsignacion":tipoAsignacion})
                #validacion campo asignadoA
                print(tabulate(gPersona.getAllData(), headers="keys", tablefmt="github"))
                input()
                break
            elif op == 2:
                tipoAsignacion = "Zona"
                asignaciones.append({"TipoAsignacion":tipoAsignacion})
                #validacion campo asignadoA
                print(tabulate(gZonas.getAllData(), headers="keys", tablefmt="github")) 
                input()   
                break
            else:
                print("Opcion no valida")
        except ValueError:
            print("El dato ingresado no es numero")         

            
                
            

