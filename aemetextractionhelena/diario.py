from conectarapi import conectarAEMET, recogerDatos
from logs import logINFO, logERROR

idfallidos = list()

# Obtener la lista de IDs fallidos
def getidfallidos():
    global idfallidos
    return idfallidos

# Formatear los datos que devuelve la API
def formatearDatos(datos, idmunicipios):
    lista = list() 
    nombre = datos.get('nombre', None)
    provincia = datos.get('provincia', None)
    predicciones = datos.get('prediccion', None).get('dia', None)

    for dia in predicciones:
        fecha = dia.get('fecha', None)
        maxima = dia.get('sensTermica', None).get('maxima',None)
        minima = dia.get('sensTermica', None).get('minima',None)
        precipitaciones = dia.get('probPrecipitacion', None)
        estadocielo = dia.get('estadoCielo', None)

        for pre, est in zip(precipitaciones,estadocielo):
            fila = {
                'nombre': nombre,
                'provincia': provincia,
                'id': idmunicipios,
                'fecha': fecha,
                'periodo': pre.get('periodo',None),
                'precipitaciones': pre.get('value',None),
                'estado_cielo': est.get('descripcion',None),
                'temp_maxima': maxima,
                'temp_minima': minima
            }
            lista.append(fila)

    return lista

def formatearJsonDatosTiempo(idmunicipios, datos):
    datos = datos[0]
    diccionario = dict()
    diccionario[idmunicipios] = formatearDatos(datos, idmunicipios)
    return diccionario

# Obtener los datos de la API
def obtenerDiario(id): 
    global idfallidos
    predicciones_finales = dict()
    
    try: 
        print(f"Obteniendo diario para {id}")
        logINFO(f"Obteniendo diario para {id}")
        url = f'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{id}'
        respuesta = conectarAEMET(url)
        datos = recogerDatos(respuesta)
          
        if datos is None:
            logERROR(f"Error al recoger los datos del id {id}")
            idfallidos.append(id)
            return None
    
        datosformateados = formatearJsonDatosTiempo(id, datos)
    
        return datosformateados
                
    except Exception as e:
        print(f"[ERROR] Fallo con el ID {id}: {e}")
    return predicciones_finales