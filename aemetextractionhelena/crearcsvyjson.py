from logs import logINFO, logERROR
from utils import formatearFechas
import pandas as pd
import datetime as dt
import json

# Crear un json
def crearJSON(nombrefichero, datos):
    with open("datos/"+nombrefichero, 'a', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print(nombrefichero," creado con exito")

# Crear el csv de predicciones 
def crearCsvPredicciones(datos):
    fechahoy = formatearFechas(dt.datetime.now())
    print(fechahoy)
    lista = list()
    # Recorer el json 
    for id ,dias in datos.items(): 
        for dia in dias: # Dia es una fila de datos
            if dia.get('fecha',None) == fechahoy: 
                print("dia ", dia.get('fecha',None), " añadido ")
                lista.append(dia) # Añadirlo a la lista de datos
    predicciones = pd.DataFrame(lista) # Convertirlo en un datafame
    predicciones.to_csv("datos/diario.csv", mode="a", header=False, index=False) # Crear el excel
    logINFO("Datos dentro del csv de Prediciones")
