from conectarapi import conectarAEMET, recogerDatos
from logs import logINFO, logERROR

idfallidos = list()

def getidfallidos():
    global idfallidos
    return idfallidos

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

def obtenerDiario(id): 
    global idfallidos
    predicciones_finales = dict()
    
    try: 
        print(f"Obteniendo diario para {id}")
        url = f'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{id}'
        respuesta = conectarAEMET(url)
        datos = recogerDatos(respuesta)
          
        if datos is None:
            idfallidos.append(id)
            return None
    
        datosformateados = formatearJsonDatosTiempo(id, datos)
    
        return datosformateados
                
    except Exception as e:
        print(f"[ERROR] Fallo con el ID {id}: {e}")
    return predicciones_finales
    # Sección critica, hay que controlar el acceso