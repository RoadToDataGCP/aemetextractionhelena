from id import obtenerId
from diario import obtenerDiario, getidfallidos
from utils import  formatearCsv, formatearJson
from crearcsvyjson import crearJSON, crearCsvPredicciones
from constantes import CABECERAPREDICIONES

def main():
   
    # Limpiar los csv y json
    formatearJson("id.json")
    formatearJson("diario.json")
    formatearJson("diariobruto.json")
    formatearCsv("diario.csv", CABECERAPREDICIONES)
        
    # Consegir los id para el diario
    print("Recoger los id")
    diccionarioid, listaid = obtenerId()

    crearJSON("id.json",diccionarioid)

    # Obtener diario
    diariofinal = dict ()

    for id in listaid:
        datosdiario = obtenerDiario(id)
        diariofinal.update(datosdiario)
    
    idsfallidos = getidfallidos()
    print("Ids fallidos: ",len(idsfallidos))

    # Obtener diarios fallidos
    for id in idsfallidos:
        datosdiario = obtenerDiario(id)
        diariofinal.update(datosdiario)
    
    crearJSON("diario.json",diariofinal)
    
    crearCsvPredicciones(diariofinal)

         
if __name__ == "__main__":
    main()