import json
import requests

def getAllData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

def getNroItem():
    data = getAllData()
    NroItem = data[-1]["NroItem"] + 1
    return(NroItem)

def getCodCampus(letras):
    codCampus = []
    data = getAllData()
    for val in data:
        letrasCodCampus = val.get("CodCampus")[0:3]
        if letrasCodCampus == letras:
            codCampus.append({
                val.get("CodCampus")     
            })
    codCampus.sort()
    consecutivo = list(codCampus[-1])
    consecutivo = int(consecutivo[0][-3:]) + 1
    return str(consecutivo)
       
def getNroFormulario():
    data = getAllData()
    NroFormulario = data[-1]["NroFormulario"] + 1
    return(NroFormulario)
        




