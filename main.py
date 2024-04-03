import os
import modules.CRUDactivos as CRUDactivos
import modules.CRUDpersonal as CRUDpersonal
import modules.CRUDzonas as CRUDzonas
import modules.CRUDasignacion as CRUDasignacion
import modules.updateMovActivos as UmovActivos

#Servidor
#json-server storage/activos.json -b 5502
#-------------------------
def menuReportes():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Movimientos de activos ---
            
            1. Listar todos los activos
            2. Listar activos por categoria
            3. Listar activos dados de baja por daño
            4. Listar activos y asignacion
            5. Listar historial de movimientos activos
            0. Regresar al menu principal   
            """)
        
        op = input("Seleccione una opcion: ")
        if op == "1" or op == "2" or op == "3" or op == "4":
            os.system("cls")
            while True:
                try:
                    nroItem = input("Ingrese el Nro Item: ")
                    nroItem = int(nroItem)
                    break
                except ValueError:
                    print("El dato ingresado no es numero")
        
        if op == "1":
            print(UmovActivos.retornoActivo(nroItem))
            input("Oprima enter para continuar....")
        elif op == "2":
            print(UmovActivos.bajaActivo(nroItem))
            input("Oprima enter para continuar....")    
        elif op == "3":
            print(UmovActivos.cambiarAsignacionActivo(nroItem))
            input("Oprima enter para continuar....") 
        elif op == "4":
            print(UmovActivos.enviarGarantiaActivo(nroItem))
            input("Oprima enter para continuar....")  
        elif op == "5":
            print(UmovActivos.enviarGarantiaActivo(nroItem))
            input("Oprima enter para continuar....")
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")

def menuMovActivos():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Movimientos de activos ---
            
            1. Retorno activo
            2. Dar de baja
            3. Cambiar de asignacion
            4. Enviar a garantia
            0. Regresar al menu principal   
            """)
        
        op = input("Seleccione una opcion: ")
        if op == "1" or op == "2" or op == "3" or op == "4":
            os.system("cls")
            while True:
                try:
                    nroItem = input("Ingrese el Nro Item: ")
                    nroItem = int(nroItem)
                    break
                except ValueError:
                    print("El dato ingresado no es numero")
        
        if op == "1":
            print(UmovActivos.retornoActivo(nroItem))
            input("Oprima enter para continuar....")
        elif op == "2":
            print(UmovActivos.bajaActivo(nroItem))
            input("Oprima enter para continuar....")    
        elif op == "3":
            print(UmovActivos.cambiarAsignacionActivo(nroItem))
            input("Oprima enter para continuar....") 
        elif op == "4":
            print(UmovActivos.enviarGarantiaActivo(nroItem))
            input("Oprima enter para continuar....")  
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")

def menuAsignacionActivos():
    flag = 1
    while flag == 1: 
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Asignacion de activos ---
            
            1. Crear asignacion
            2. Buscar asignacion
            0. Regresar al menu principal   
            """)
        
        op = input("Seleccione una opcion: ")
        if op == "1" or op == "2":
            os.system("cls")
            while True:
                try:
                    nroItem = input("Ingrese el Nro Item: ")
                    nroItem = int(nroItem)
                    break
                except ValueError:
                    print("El dato ingresado no es numero")
            
        if op == "1":
            print(CRUDasignacion.postAsignacion(nroItem))
            input("Oprima enter para continuar....")
        elif op == "2":
            CRUDasignacion.findAsignacion(nroItem)
            input("Oprima enter para continuar....")    
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")

def menuZonas():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Zonas ---
            
            1. Agregar
            2. Editar
            3. Eliminar
            4. Buscar
            0. Regresar al menu principal   
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(CRUDzonas.postZonas())
            input("Oprima enter para continuar....")
        elif op == "2":
            print(CRUDzonas.updateZonas())
            input("Oprima enter para continuar....")    
        elif op == "3":
            input("Oprima enter para continuar....") 
        elif op == "4":
            CRUDzonas.findZonas()
            input("Oprima enter para continuar....")     
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")

def menuPersonal():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Personal ---
            
            1. Agregar
            2. Editar
            3. Eliminar
            4. Buscar
            0. Regresar al menu principal   
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(CRUDpersonal.postPersonal())
            input("Oprima enter para continuar....")
        elif op == "2":
            print(CRUDpersonal.updatePersonal())
            input("Oprima enter para continuar....")    
        elif op == "3":
            input("Oprima enter para continuar....") 
        elif op == "4":
            CRUDpersonal.findPersonal()
            input("Oprima enter para continuar....")     
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")

def menuActivos():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Activos ---
            
            1. Agregar
            2. Editar
            3. Eliminar
            4. Buscar
            0. Regresar al menu principal   
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(CRUDactivos.postActivos())
            input("Oprima enter para continuar....")
        elif op == "2":
            print(CRUDactivos.updateActivos())
            input("Oprima enter para continuar....")    
        elif op == "3":
            input("Oprima enter para continuar....") 
        elif op == "4":
            CRUDactivos.findActivos()
            input("Oprima enter para continuar....")     
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")

if (__name__=="__main__"):
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
        
            +-+-+-+-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+
            |S|I|S|T|E|M|A| |G|&|C| |D|E| |I|N|V|E|N|T|A|R|I|O| |C|A|M|P|U|S|L|A|N|D|S|
            +-+-+-+-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+

            --- Menu Principal ---

            1. Activos
            2. Personal
            3. Zonas
            4. Asignacion de activos
            5. Reportes
            6. Movimiento de activos
            0. Salir
            """)

        op = input("Seleccione una opcion: ")

        if op == "1":
            menuActivos()
        elif op == "2":    
            menuPersonal()
        elif op == "3":    
            menuZonas()
        elif op == "4":  
            menuAsignacionActivos() 
        elif op == "5":    
            menuReportes()
        elif op == "6":   
            menuMovActivos()
        elif op == "0":
            print("Gracias por utilizar el programa")
            flag = 0   
        else:
            print("No es una opcion valida")
            input("Oprima enter para ingresar nueva opcion....")
