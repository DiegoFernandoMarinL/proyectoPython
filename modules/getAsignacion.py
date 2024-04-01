import modules.getActivos as gActivos

def getNroAsignacion(nroItem):
    data = gActivos.getAllData()
    dato = []
    for val in data:
        if val.get("NroItem") == nroItem:
            dato.append(val)
            if dato[0]["asignaciones"]:
                NroAsignacion = int(dato[0]["asignaciones"][-1]["NroAsignacion"]) + 1
            else:
                NroAsignacion = 1
    return(NroAsignacion)
