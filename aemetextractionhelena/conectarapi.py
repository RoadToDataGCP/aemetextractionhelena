from logs import logERROR, logINFO
from constantes import TODAS_API_KEY
import requests as rq
import time 


# Mensaje de error en el log y en la consola
def mensajeError (mensaje):
    logERROR(mensaje)
    print(mensaje)
    time.sleep(30)

# Cambiar de Api Key
def gestionarApiKey(APY_KEY,api_key_fallo):
    if (api_key_fallo == APY_KEY[0] ):
        return APY_KEY[1]
    else:
        return APY_KEY[0]

def conectarAEMET(url):
    # Intentar conectarse hasta 5 veces
    api_key = gestionarApiKey(TODAS_API_KEY,TODAS_API_KEY[1])
    for _ in range(5):
        try:
            parametros = {
                'api_key': api_key
            }
            respuesta = rq.get(url, params=parametros, timeout=30)
            print(f"{respuesta} ")
            if respuesta.status_code == 200:
                print("Conectado")
                logINFO("Conectado a la api de la AEMET")
                return respuesta.json()
            # Trata de errores 
            elif respuesta.status_code == 400:
                mensajeError("Error: petición erronea")
                api_key = gestionarApiKey(TODAS_API_KEY,api_key)
            elif respuesta.status_code == 401:
                mensajeError("Error: no tienes autorización")
                api_key = gestionarApiKey(TODAS_API_KEY,api_key) 
            elif respuesta.status_code == 403:
                mensajeError("Error: no tines permisos") 
                api_key = gestionarApiKey(TODAS_API_KEY,api_key)
            elif respuesta.status_code == 404:
                mensajeError("Error: endpoint erroneo")
                api_key = gestionarApiKey(TODAS_API_KEY,api_key)
            elif respuesta.status_code == 429:
                mensajeError("Error: demasidas peticiones")  
                api_key = gestionarApiKey(TODAS_API_KEY,api_key)
            elif respuesta.status_code == 500:
                mensajeError("Error: en el servidor de la api")
                api_key = gestionarApiKey(TODAS_API_KEY,api_key) 
            elif respuesta.status_code == 502:
                mensajeError("Error: servidor caido") 
                api_key = gestionarApiKey(TODAS_API_KEY,api_key)
            else:
                mensajeError("Error: otro error") 
                api_key = gestionarApiKey(TODAS_API_KEY,api_key)
        except Exception as e:
            mensajeError(f"Error: {e}") 
            api_key = gestionarApiKey(TODAS_API_KEY,api_key)
    return None

def recogerDatos(respuesta):
    try:
        # Respuesta vacia por un error en la api
        if respuesta is None:
            logERROR("Respuesta vacia,, por error en la conexión a la API")
            print("Respuesta vacia, por error en la conexión a la API")
            return None
        
        # Coger la url de datos y comprobar que no estan vacios
        url = respuesta.get('datos')
        if url is None:
            logERROR("El campo datos no existe")
            print("En la respuesta obtenida por la API no existe el campo datos")
            return None
        
        # Conectarme a la api con la url de los datos
        datos = conectarAEMET(url)
        logINFO("Datos recogidos con exito")
        print("Datos recogidos")

        # Devolver los datos 
        return datos
    
    except Exception as e:
        print(f"Error: {e}")
    return None 
