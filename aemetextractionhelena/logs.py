import logging

# Configuracion de los logs 
logging.basicConfig (
    filename='datos/logs.log',     
    level=logging.INFO ,
    filemode= 'w', # Sobreescribe el archivo
    datefmt='%Y-%m-%d %H:%M:%S')

# Log de información
def logINFO(mesaje):
    logging.info(mesaje)

# Log de error 
def logERROR(mesaje):
    logging.error(mesaje)
