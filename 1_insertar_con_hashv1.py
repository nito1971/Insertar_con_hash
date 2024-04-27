import os
import hashlib


ruta_origen = "/mnt/local/datos/Contras/Collection #2-#5 & Antipublic/Collection 1"
ruta_destino = "/mnt/local/datos/Contras/TXT"
extensiones_excluidas =["sql", "xlxs", "docx", "doc", "html"]


def get_hash(input_string):
    try:
        return hashlib.sha384(input_string.encode()).hexdigest()
    except:
        return None



def recorrer_directorio(ruta_directorio):
    with open(os.path.join(ruta_destino, "Collection_1.txt"), "a+", encoding="latin1") as contras_file:        
            for root, dirs, files in os.walk(ruta_directorio):
                try:
                    for file in files:
                        if not file.endswith(tuple(extensiones_excluidas)):                            
                            ruta_completa = os.path.join(root, file)
                            with open(ruta_completa, "r", encoding="latin1") as archivo:
                                for linea in archivo:
                                    linea = get_hash(linea)
                                    print(linea)                                          
                                    #contras_file.write(linea + "\n")                               
                            
                except FileNotFoundError as e:
                    print(f"Error al procesar archivo: {e}")
                    
      

a = recorrer_directorio(ruta_origen)