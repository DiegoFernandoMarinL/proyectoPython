import os
import modules.CRUDactivos as CRUDactivos

import modules.getActivos as gActivos

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
            input("Oprima una tecla para continuar....")
        elif op == "2":
            CRUDactivos.updateActivos()
            input("Oprima una tecla para continuar....")    
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima una tecla para ingresar nueva opcion....")

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
            print("falta anexar")
        elif op == "3":    
            print("falta anexar")
        elif op == "4":  
            print("falta anexar") 
        elif op == "5":    
            print("falta anexar")
        elif op == "6":   
            print(type(gActivos.getAllData()))
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "0":
            print("Gracias por utilizar el programa")
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima una tecla para ingresar nueva opcion....")
