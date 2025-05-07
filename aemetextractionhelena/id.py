from logs import logERROR, logINFO
import pandas as pd


def formatearJsonId(datos_id):
    diccionarioid= dict() # Para el JSON
    listaid = list() # Para pasárselos a la API

    for _,linea in datos_id.iterrows(): # Recorrer linea por linea del excel
        id = str(linea['CPRO']).zfill(2) + str(linea['CMUN']).zfill(3) # Sacra el id 
        diccionarioid[linea["NOMBRE"]] = id 
        listaid.append(id) 

    return diccionarioid, listaid

def obtenerId():
    # Obtener los datos de los municipios del excel
    datos_id= pd.DataFrame(pd.read_excel("datos/diccionario24.xlsx", skiprows=1))

    # Crear una lista y el JSON de los IDs
    diccionarioid, listaid = formatearJsonId(datos_id)

    if listaid is None:
        logERROR("Error al recoger los IDs")
    else:
        logINFO("IDs recogidos con éxito")
        
    return diccionarioid, listaid [0:10]