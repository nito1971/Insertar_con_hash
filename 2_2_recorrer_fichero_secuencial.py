import pymongo
import os
import time
ruta_directorio = "/mnt/local/datos/Contras/archivos_partidos"

def insert_mongo(_id, datos):
    client = pymongo.MongoClient("localhost", 27019)
    db = client._constructor_args
    collection = db.tcontras
    collection.insert_one({"_id": _id, "datos": datos})

def recorre_directorio(directorio):
    for root, dirs, files in os.walk(directorio):
        print(f"Directorio actual: {root}")
        for file in files:
            ruta =  os.path.join(root, file)
            print(ruta)
            inicio = time.time()
            try:
                with open(ruta, "r") as f:
                    for linea in f:
                        linea_a_hashear = linea.rstrip("\n")                    
                        _id = linea_a_hashear                   
                        datos = linea_a_hashear              
                        insert_mongo(_id, datos)
                        #print(f"Usuario: {usuario} - Passwd: {passwd}")
                                
                    os.remove(ruta)                
                    print(f"{file} ha sido eliminado.")
                    final = time.time()
                    tiempo_total = (final - inicio)
                    print(f"Tiempo total de ejecución: {tiempo_total} segundos.")
                    #print(f"Quedan {numero_archivos()} archivos aún")
            except Exception as e:
                print(e)
                return False
if __name__ == "__main__":
    recorre_directorio(ruta_directorio)