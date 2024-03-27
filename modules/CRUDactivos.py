import os
import re
import json
import requests
import modules.getActivos as gActivos
import modules.getTipoActivos as gTipoActivos
import modules.getMarcas as gMarcas
import modules.getCategorias as gCategorias
import modules.getEstados as gEstados

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
                    break
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 4 caracteres como minimo")
        except Exception as error:
            print(error)         
    #valida campo codCampus
    print(f"""
        --- Tipo de activos ---""")
    for i, val in enumerate(gTipoActivos.getTipoActivos()):
        print(f"  {i+1}. {val.get('Nombre').title()}")
    print()    
    while True:
        idTipoActivo = input("Seleccione tipo de activo: ")
        if idTipoActivo == "1":
            letras = "MON"
            break
        elif idTipoActivo == "2":
            letras = "CPU"
            break
        elif idTipoActivo == "3":
            letras = "TEC"
            break
        elif idTipoActivo == "4":
            letras = "MOU"
            break
        elif idTipoActivo == "5":
            letras = "AC0"
            break
        elif idTipoActivo == "6":
            letras = "PT0"
            break
        elif idTipoActivo == "7":
            letras = "TV0"
            break
        elif idTipoActivo == "8":
            letras = "MA0"
            break

                # elif idTipoActivo == "0":
                #     if(not newActivo.get("CodCampus")):
                #         dato = input("Codigo Campus (Formato ABC123): ")
                #         #valida que el campo no este vacio y que tenga minimo 6 caracteres
                #         if(re.match(r'^(?!\s*$)[A-Z]{3}\d{3}$', dato) is not None):
                #             newActivo["CodCampus"] = dato
                #         else:
                #             raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 6 caracteres como minimo")
                #     break

        else:
            print("No es una opcion valida")
            input("Oprima una tecla para ingresar nueva opcion....")

    dato = letras+gActivos.getCodCampus(letras)
    if idTipoActivo == "6" or idTipoActivo == "7" or idTipoActivo == "8":
        dato = letras+"0"+gActivos.getCodCampus(letras)     
    print("Codigo campus: ", dato) 
    newActivo["CodCampus"] = dato
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
    #valida campo marca
    print(f"""
          --- Marcas ---""")
    for i, val in enumerate(gMarcas.getMarcas()):
        print(f"  {i+1}. {val.get('Nombre').title()}")
    print()
    while True:
        try:
            op = input("Seleccione marca: ")
            op = int(op)
            if op > 0 and op <= len(gMarcas.getMarcas()):
                newActivo["idMarca"] = str(op)
                break
            else:
                print("No es una opcion valida")
                input("Oprima una tecla para ingresar nueva opcion....")
        except ValueError:
            print("El dato ingresado no es numero")
    #valida campo categoria
    print(f"""
          --- Categorias ---""")
    for i, val in enumerate(gCategorias.getCategorias()):
        print(f"  {i+1}. {val.get('Nombre').title()}")
    print()
    while True:
        try:
            op = input("Seleccione categoria: ")
            op = int(op)
            if op > 0 and op <= len(gCategorias.getCategorias()):
                newActivo["idCategoria"] = str(op)
                break
            else:
                print("No es una opcion valida")
                input("Oprima una tecla para ingresar nueva opcion....")
        except ValueError:
            print("El dato ingresado no es numero")                
    #valida campo tipo
    newActivo["idTipo"] = idTipoActivo
    #valida campo valor unitario
    while True:
        try:
            op = input("Valor unitario: ")
            op = int(op)
            newActivo["ValorUnitario"] = str(op)
            break
        except ValueError:
            print("El dato ingresado no es numero")                
    #valida campo estado
    print(f"""
          --- Estados ---""")
    for i, val in enumerate(gEstados.getEstados()):
        print(f"  {i+1}. {val.get('Nombre').title()}")
    print()
    while True:
        try:
            op = input("Seleccione estado: ")
            op = int(op)
            if op > 0 and op <= len(gEstados.getEstados()):
                newActivo["idEstado"] = str(op)
                break
            else:
                print("No es una opcion valida")
                input("Oprima una tecla para ingresar nueva opcion....")
        except ValueError:
            print("El dato ingresado no es numero")
    #valida campo historial activos
    hisActivos = []
    newActivo["historialActivos"] = hisActivos  
    #valida campo asignaciones
    asigActivos = []
    newActivo["asignaciones"] = asigActivos 

    print(newActivo)    
    input()        