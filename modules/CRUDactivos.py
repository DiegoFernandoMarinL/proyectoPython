import os
import re
import json
import requests
import modules.getActivos as gActivos
import modules.getTipoActivos as gTipoActivos
import modules.getMarcas as gMarcas

def postActivos():
    os.system("cls")
    newActivo = dict()
    #valida campo NroItem
    print("Nro item: ", gActivos.getNroItem())
    newActivo["NroItem"] = gActivos.getNroItem()
    #valida campo codigo transaccion
    print("Codigo transaccion: ", 327)
    newActivo["CodTransaccion"] = 327
    while True:
        try:
            #valida campo NroSerial
            if(not newActivo.get("NroSerial")):
                dato = input("Nro serial (de no tener colocar sin serial): ")
                #valida que el campo no este vacio y que tenga minimo 4 caracteres
                if(re.match(r'^(?!\s+$).{4,}$', dato) is not None):
                    newActivo["NroSerial"] = dato
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 4 caracteres como minimo")
            #valida campo codCampus
            for i, val in enumerate(gTipoActivos.getTipoActivos()):
                print(f"  {i+1}. {val.get('Nombre')}")
            print(f"  0. Otro")
            while True:
                op = input("Seleccione tipo de activo: ")
                if op == "1":
                    letras = "MON"
                    break
                elif op == "2":
                    letras = "CPU"
                    break
                elif op == "3":
                    letras = "TEC"
                    break
                elif op == "4":
                    letras = "MOU"
                    break
                elif op == "5":
                    letras = "AC0"
                    break
                elif op == "6":
                    letras = "PT0"
                    break
                elif op == "7":
                    letras = "TV0"
                    break
                elif op == "8":
                    letras = "MA0"
                    break
                elif op == "0":
                    if(not newActivo.get("CodCampus")):
                        dato = input("Codigo Campus (Formato ABC123): ")
                        #valida que el campo no este vacio y que tenga minimo 6 caracteres
                        if(re.match(r'^(?!\s*$)[A-Z]{3}\d{3}$', dato) is not None):
                            newActivo["CodCampus"] = dato
                        else:
                            raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 6 caracteres como minimo")
                    break
                else:
                    print("No es una opcion valida")
                    input("Oprima una tecla para ingresar nueva opcion....")

            if op != "0":
                dato = letras+gActivos.getCodCampus(letras)
                if op == "6" or op == "7" or op == "8":
                    dato = letras+"0"+gActivos.getCodCampus(letras)     
                print("Codigo campus: ", dato) 
                newActivo["CodCampus"] = dato
            break
        except Exception as error:
            print(error) 

    #valida campo Nro formulario
    print("Nro Formulario: ", gActivos.getNroFormulario())
    newActivo["NroFormulario"] = gActivos.getNroFormulario()
    #valida campo nombre  
    dato = input("Nombre activo: ")
    newActivo["Nombre"] = dato
    #valida campo proveedor
    print("Proveedor:  Compumax Computer ")
    newActivo["Proveedor"] = "Compumax Computer "
    #valida campo empresa responsable
    print("Empresa responsable:  Campuslands")
    newActivo["EmpresaResponsable"] = "Campuslands"
    for i, val in enumerate(gMarcas.getMarcas()):
        print(f"  {i+1}. {val.get('Nombre')}")
    print(f"  0. Otro")
    
    print(newActivo)    
    input()        