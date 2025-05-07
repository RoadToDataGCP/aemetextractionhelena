from logs import logINFO
import pandas as pd


# Formatear las fechas 
def formatearFechas(fecha):
    logINFO(f"Fecha {fecha} formateada")
    return fecha.strftime("%Y-%m-%dT00:00:00")

#Limpiar los csv
def formatearCsv(nombre, cabecera):
    logINFO(f"CSV {nombre} limpio")
    df = pd.DataFrame(columns= cabecera)
    df.to_csv("datos/"+nombre, mode="w", index=False)

#Limpiar los json
def formatearJson(nombre):
    logINFO(f"JSON {nombre} limpio")
    datos = ''
    with open("datos/"+nombre, 'w', encoding='utf-8') as archivo:
       pass
