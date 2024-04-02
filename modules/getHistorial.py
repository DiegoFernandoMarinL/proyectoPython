import datetime
import modules.getActivos as gActivos

def getHistorial(nroItem,historial,tipoMov,idResponsableMov):
    data = gActivos.getAllData()
    dato = []
    for val in data:
        if val.get("NroItem") == nroItem:
            dato.append(val)
            if dato[0]["historialActivos"]:
                NroHistorial = int(dato[0]["historialActivos"][-1]["NroId"]) + 1
            else:
                NroHistorial = 1

    fechaHora = datetime.datetime.now()   
    fechaHora = fechaHora.strftime("%Y-%m-%d %H:%M")
    historial.append({
        "NroId":NroHistorial,
        "Fecha":fechaHora,
        "tipoMov":tipoMov,
        "idRespMov":idResponsableMov
    })            
    return(historial)