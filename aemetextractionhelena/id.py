from logs import logERROR, logINFO
import pandas as pd


def formatearJsonId(datos_id):
    diccionarioid= dict() # Para el json
    listaid = list() # Para pasarselos a la api

    for _,linea in datos_id.iterrows(): # Recorrer linea por linea del excel
        id = str(linea['CPRO']).zfill(2) + str(linea['CMUN']).zfill(3) # Sacra el id 
        diccionarioid[linea["NOMBRE"]] = id # Añadirlo al dicionario junto al nombre
        listaid.append(id) # Añadirlo a la lista de id

    return diccionarioid, listaid

def obtenerId():
    # Obtener los datos de los municipios del excel
    datos_id= pd.DataFrame(pd.read_excel("aemetextractionhelena/datos/diccionario24.xlsx", skiprows=1))

    # Crear una lista y el json de lo ids
    diccionarioid, listaid = formatearJsonId(datos_id)

    if listaid is None:
        logERROR("Error al recojer los ids")
    else:
        logINFO("Ids recojidos con éxito")
        
    return diccionarioid, listaid [0:10]