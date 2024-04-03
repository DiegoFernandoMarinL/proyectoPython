from tabulate import tabulate
import os
import modules.getActivos as gActivos
import modules.getCategorias as gCategorias

def historialActivos():
    os.system("cls")
    while True:
        try:
            nroItem = input("Ingrese el Nro Item: ")
            nroItem = int(nroItem)
            break
        except ValueError:
            print("El dato ingresado no es numero")
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            historial = val.get("historialActivos")    
            print(f"""
-----------Historial activo----------------
{tabulate(historial, headers="keys", tablefmt="github")}
""")
            
def allActivos():
    os.system("cls")
    activo = []    
    for val in gActivos.getAllData():
        activo.append({
            "Nro Item": val.get("NroItem"),
            "Cod Transaccion": val.get("CodTransaccion"),
            "Nro Serial": val.get("NroSerial"),
            "Cod Campus": val.get("CodCampus"),
            "Nro Formulario": val.get("NroFormulario"),
            "Nombre": val.get("Nombre"),
            "Proveedor": val.get("Proveedor"),
            "Empresa Responsable": val.get("EmpresaResponsable"),
            "Valor Unitario": val.get("ValorUnitario")
        }) 

    print(f"""
-----------Activos----------------
{tabulate(activo, headers="keys", tablefmt="github")}
""")              
            
def getActivosCategoria():
    os.system("cls")
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
                break
            else:
                print("No es una opcion valida")
                input("Oprima enter para ingresar nueva opcion....")
        except ValueError:
            print("El dato ingresado no es numero") 

    activo = []    
    for val in gActivos.getAllData():
        if val.get("idCategoria") == str(op):
            activo.append({
                "Nro Item": val.get("NroItem"),
                "Cod Transaccion": val.get("CodTransaccion"),
                "Nro Serial": val.get("NroSerial"),
                "Cod Campus": val.get("CodCampus"),
                "Nro Formulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "Valor Unitario": val.get("ValorUnitario")
            })      
    print(f"""
-----------Activos----------------
{tabulate(activo, headers="keys", tablefmt="github")}
""")                   

def getActivosBaja():
    os.system("cls")
    activo = []    
    for val in gActivos.getAllData():
        if val.get("idEstado") == "2":
            activo.append({
                "Nro Item": val.get("NroItem"),
                "Cod Transaccion": val.get("CodTransaccion"),
                "Nro Serial": val.get("NroSerial"),
                "Cod Campus": val.get("CodCampus"),
                "Nro Formulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "Valor Unitario": val.get("ValorUnitario")
            })      
    print(f"""
-----------Activos----------------
{tabulate(activo, headers="keys", tablefmt="github")}
""")  