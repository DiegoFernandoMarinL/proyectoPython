from tabulate import tabulate
import os
import re
import json
import requests
import modules.getPersonal as gPersonal

def postPersonal():
    os.system("cls")
    newPersona = dict()
    #valida nroId
    while True:
        try:
            if(not newPersona.get("nroId (CC, Nit)")):
                dato = input("Nro cedula o nit: ")
                #valida que el campo no este vacio y que tenga minimo 4 digitos
                if(re.match(r'^\d{4,}$', dato) is not None):
                    data = gPersonal.getNroCedulaNit(dato)
                    if (data):
                        print()
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        print()
                        raise Exception("El numero cedula/nit del personal ya existe")
                    else:
                        newPersona["nroId (CC, Nit)"] = dato
                        break
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 4 digitos como minimo")
        except Exception as error:
            print(error)
    #valida nombre
    dato = input("Nombre: ")
    newPersona["Nombre"] = dato        
    #valida email
    while True:
        try:    
            if(not newPersona.get("Email")):
                email = input("Email: ")
                if(re.match(r'^[^@\s]+@[^@\s]+$', email) is not None):
                    data = gPersonal.getEmail(email)
                    if (data):
                        print()
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        print()
                        raise Exception("El email del personal ya existe")
                    else:
                        newPersona["Email"] = email
                        break
                else:
                    raise Exception("El email del empleado no cumple con el estandar establecido, no es un correo valido")
        except Exception as error:
            print(error)        
    #valida telefono
    telefonos = []
    while True:
        try:
            #valida movil
            dato = input("Telefono movil: (de no tener dar enter) ")
            #valida que el campo no este vacio y que tenga minimo 8 digitos
            if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                telefonos.append({"movil":{"id":"1", "num":dato}})
                break
            else:
                raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")
        except Exception as error:
            print(error)
    while True:    
        try:
            #valida casa
            dato = input("Telefono casa: (de no tener dar enter) ")
            #valida que el campo no este vacio y que tenga minimo 8 digitos
            if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                telefonos.append({"casa":{"id":"2","num":dato}})
                break
            else:
                raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")        
        except Exception as error:
            print(error)
    while True: 
        try:               
            #valida personal
            dato = input("Telefono personal: (de no tener dar enter) ")
            #valida que el campo no este vacio y que tenga minimo 8 digitos
            if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                telefonos.append({"personal":{"id":"3","num":dato}})
                break
            else:
                raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")    
        except Exception as error:
            print(error)
    while True:
        try:                
            #valida oficina
            dato = input("Telefono oficina: (de no tener dar enter) ")
            #valida que el campo no este vacio y que tenga minimo 8 digitos
            if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                telefonos.append({"oficina":{"id":"4","num":dato}})
                break
            else:
                raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")    
        except Exception as error:
            print(error)

    newPersona["Telefonos"] = telefonos

    peticion = requests.post("http://154.38.171.54:5502/personas", data=json.dumps(newPersona))
    if(peticion.status_code == 201 or peticion.status_code == 200):
        return("Personal creado correctamente")
    else:
        return peticion.status_code

def updatePersonal():
    os.system("cls")
    while True:
        try:
            nroCC = input("Ingrese el Nro cedula o nit a editar: ")
            nroCC = int(nroCC)
            break
        except ValueError:
            print("El dato ingresado no es numero")
    newPersona = dict()
    getCC = []
    for val in gPersonal.getAllData():
        if val.get("nroId (CC, Nit)") == str(nroCC):
            newPersona = val
            getCC.append({
                "id":val.get("id"),
                "Nro cedula/nit":val.get("nroId (CC, Nit)"),
                "Nombre":val.get("Nombre"),
                "Email":val.get("Email"),
            })
            telefonos = val.get("Telefonos")
            break
    if not newPersona:
        return "No se encontro el nro cedula o nit"
    else:
        id = getCC[0]["id"]         
        print()    
        print(tabulate(getCC,headers="keys",tablefmt="github")) 
        while True:
            print(f"""
                --- Editar datos ---
                
                1. Nro cedula/nit
                2. Nombre
                3. Email
                4. Telefonos  
                0. Atras  
                """)

            op = input("Seleccione un campo a editar: ")
                
            if op == "1":
                #valida nroId
                while True:
                    try:
                        if(newPersona.get("nroId (CC, Nit)")):
                            dato = input("Nro cedula o nit: ")
                            #valida que el campo no este vacio y que tenga minimo 4 digitos
                            if(re.match(r'^\d{4,}$', dato) is not None):
                                data = gPersonal.getNroCedulaNit(dato)
                                if (data):
                                    print()
                                    print(tabulate(data, headers="keys", tablefmt="github"))
                                    print()
                                    raise Exception("El numero cedula/nit del personal ya existe")
                                else:
                                    newPersona["nroId (CC, Nit)"] = dato
                                    break
                            else:
                                raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 4 digitos como minimo")
                    except Exception as error:
                        print(error)
                print("Dato actualizado correctamente") 
                input("Oprima enter para continuar....")
                os.system("cls")
            elif op == "2":
                    #valida nombre
                    dato = input("Nombre: ")
                    newPersona["Nombre"] = dato 
                    print("Dato actualizado correctamente") 
                    input("Oprima enter para continuar....")
                    os.system("cls")
            elif op == "3":
                    #valida email
                    while True:
                        try:    
                            if(newPersona.get("Email")):
                                email = input("Email: ")
                                if(re.match(r'^[^@\s]+@[^@\s]+$', email) is not None):
                                    data = gPersonal.getEmail(email)
                                    if (data):
                                        print()
                                        print(tabulate(data, headers="keys", tablefmt="github"))
                                        print()
                                        raise Exception("El email del personal ya existe")
                                    else:
                                        newPersona["Email"] = email
                                        break
                                else:
                                    raise Exception("El email del empleado no cumple con el estandar establecido, no es un correo valido")
                        except Exception as error:
                            print(error)
                    print("Dato actualizado correctamente") 
                    input("Oprima enter para continuar....")
                    os.system("cls")
            elif op == "4":
                    #valida telefono
                    print(f"""
                --- Telefonos ---
                          
                1. Movil
                2. Casa
                3. Personal
                4. Oficina  
                          """)
                    op = input("Seleccione telefono a cambiar: ")
                    if op == "1":
                        while True:
                            try:
                                #valida movil
                                dato = input("Telefono movil: (de no tener dar enter) ")
                                #valida que el campo no este vacio y que tenga minimo 8 digitos
                                if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                                    telefonos[int(op)-1]["movil"]["num"] = dato
                                    break
                                else:
                                    raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")
                            except Exception as error:
                                print(error)
                    elif op == "2":
                        while True:    
                            try:
                                #valida casa
                                dato = input("Telefono casa: (de no tener dar enter) ")
                                #valida que el campo no este vacio y que tenga minimo 8 digitos
                                if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                                    telefonos[int(op)-1]["casa"]["num"] = dato
                                    break
                                else:
                                    raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")        
                            except Exception as error:
                                print(error)
                    elif op == "3":
                        while True: 
                            try:               
                                #valida personal
                                dato = input("Telefono personal: (de no tener dar enter) ")
                                #valida que el campo no este vacio y que tenga minimo 8 digitos
                                if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                                    telefonos[int(op)-1]["personal"]["num"] = dato
                                    break
                                else:
                                    raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")    
                            except Exception as error:
                                print(error)  
                    elif op == "4":
                        while True:
                            try:                
                                #valida oficina
                                dato = input("Telefono oficina: (de no tener dar enter) ")
                                #valida que el campo no este vacio y que tenga minimo 8 digitos
                                if(re.match(r'^(?:\d{8,}|)$', dato) is not None):
                                    telefonos[int(op)-1]["oficina"]["num"] = dato
                                    break
                                else:
                                    raise Exception(f"{dato} no cumple con el estandar establecido, debe tener 8 digitos como minimo sin espacios")    
                            except Exception as error:
                                print(error)
                    else:
                        print("No es una opcion valida")
                        input("Oprima enter para ingresar nueva opcion....")
            
                    newPersona["Telefonos"] = telefonos
                    print("Dato actualizado correctamente") 
                    input("Oprima enter para continuar....")
                    os.system("cls")                               
            elif op == "0":
                break    
            else:
                print("No es una opcion valida")
                input("Oprima enter para ingresar nueva opcion....")       

        peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(newPersona))
        if(peticion.status_code == 201 or peticion.status_code == 200):
            return("Personal actualizado correctamente")
        else:
            return peticion.status_code

