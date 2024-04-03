import json
import requests
import modules.getActivos as gActivos
import modules.getHistorial as gHistorial
import modules.CRUDasignacion as CRUDasignaciones

def retornoActivo(nroItem):
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

def bajaActivo(nroItem):
    updateActivo = dict()
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            updateActivo = val 
            id = updateActivo["id"]
            idEstado = val.get("idEstado")
            if idEstado == "0": #no asignado
                updateActivo["idEstado"] = "2" # dado de baja
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

def cambiarAsignacionActivo(nroItem):
    updateActivo = dict()
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            updateActivo = val 
            idEstado = val.get("idEstado")
            if idEstado == "1": # asignado
                CRUDasignaciones.postAsignacion(nroItem)
                for val in gActivos.getAllData():
                    if val.get("NroItem") == nroItem:
                        updateActivo = val
                        id = updateActivo["id"]
                updateActivo["idEstado"] = "1" # asignado
                updateActivo["historialActivos"][-1]["tipoMov"] = "4" # reasignado
                peticion = requests.put(f"http://localhost:5501/activos/{id}", data=json.dumps(updateActivo))
                if(peticion.status_code == 201 or peticion.status_code == 200):
                    return("Activo reasignado correctamente")
                else:
                    return peticion.status_code
            elif idEstado == "2": #dado de baja
                return "El activo esta dado de baja no se puede reasignar"
            elif idEstado == "3": #reparacion
                return "Activo en reparacion o garantia no se puede reasignar"
            elif idEstado == "0": #no asignado
                return "Activo no esta asignado debe crear una asignacion"
            
def enviarGarantiaActivo(nroItem):
    updateActivo = dict()
    for val in gActivos.getAllData():
        if val.get("NroItem") == nroItem:
            updateActivo = val 
            id = updateActivo["id"]
            idEstado = val.get("idEstado")
            if idEstado == "0" or idEstado == "1": #no asignado o asignado
                updateActivo["idEstado"] = "3" # reparacion
                historial = val.get("historialActivos")
                tipoMov = "3" # en garantia
                idResponsableMov = "Campuslands"
                historial = gHistorial.getHistorial(nroItem,historial,tipoMov,idResponsableMov)
                updateActivo["historialActivos"] = historial

                peticion = requests.put(f"http://localhost:5501/activos/{id}", data=json.dumps(updateActivo))
                if(peticion.status_code == 201 or peticion.status_code == 200):
                    return("Activo en garantia correctamente")
                else:
                    return peticion.status_code
            elif idEstado == "2": #dado de baja
                return "El activo esta dado de bajo no se puede enviar a garantia"
            elif idEstado == "3": #reparacion
                return "El activo ya estaba en garantia"

            
     
