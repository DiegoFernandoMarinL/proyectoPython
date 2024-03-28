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
            #valida campo NroSerial
            if(not newPersona.get("nroId (CC, Nit)")):
                dato = input("Nro cedula o nit: ")
                #valida que el campo no este vacio y que tenga minimo 4 digitos
                if(re.match(r'^\d{4,}$', dato) is not None):
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
            if(not newPersona.get("Telefonos":"movil")):
                dato = input("Telefono movil: ")
                #valida que el campo no este vacio y que tenga minimo 8 digitos
                if(re.match(r'^\d{8,}$', dato) is not None):
                    telefonos.append({"movil":{"num":dato}})
                    newPersona["Telefonos"] = telefonos
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 8 digitos como minimo")
            #valida casa
            if(not newPersona.get("Telefonos":"casa")):
                dato = input("Telefono casa: ")
                #valida que el campo no este vacio y que tenga minimo 8 digitos
                if(re.match(r'^\d{8,}$', dato) is not None):
                    telefonos.append({"casa":{"num":dato}})
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 8 digitos como minimo")        
            #valida personal
            if(not telefonos.get("personal")):
                dato = input("Telefono personal: ")
                #valida que el campo no este vacio y que tenga minimo 8 digitos
                if(re.match(r'^\d{8,}$', dato) is not None):
                    telefonos.append({"personal":{"num":dato}})
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 8 digitos como minimo")    
            #valida oficina
            if(not telefonos.get("oficina")):
                dato = input("Telefono oficina: ")
                #valida que el campo no este vacio y que tenga minimo 8 digitos
                if(re.match(r'^\d{8,}$', dato) is not None):
                    telefonos.append({"oficina":{"num":dato}})
                    break
                else:
                    raise Exception(f"{dato} no cumple con el estandar establecido, no puede ser vacio y debe tener 8 digitos como minimo")    
        except Exception as error:
            print(error)

    newPersona["Telefonos"] = telefonos

    print(newPersona)
    input()        
