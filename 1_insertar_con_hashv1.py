'''
Script que recorre distintos tipos de ficheros y
extrae su contenido y lo inserta en un archivo evitando duplicados.
Para ello, utiliza un hash para cada linea del fichero y se guarda en un archivo txt.
Al inicio se lee el archivo txt para obtener los hash ya insertados.
A continuación se recorre el directorio y se extrae su contenido.
Se comprueba si el hash ya existe en el archivo txt.
Con ello evitamos repetir todo el proceso en el caso de que el volumen de archivos de entrada
sea grande y se tenga que comenzar todo el proceso desde cero.
Si no existe, se inserta en el archivo txt.
Los datos de entrada se encuentran en  un directorio.
El archivo de salida es un archivo txt.
Los hash se leen desde y escriben en un archivo txt.
'''

import os
import hashlib

## Define the origin directory and the destination directory for writing output files.
ruta_origen = "/mnt/10.0.1.20/datos/Contras/Sin_procesar"
ruta_destino = "/mnt/10.0.1.20/datos/Contras/procesado"

## Define a list of file extensions to exclude from processing
extensiones_excluidas = ["sql", "xlxs", "docx", "doc", "html"]
contras_ya_vistas  = []  # Initialize an empty list for storing hashes

def insertar_en_archivo_hash(hash):
    """
    Write the hash to a file.
    :param hash: The hash to be written
    """
    with open(os.path.join(ruta_destino, "hashes.txt"), "a+") as archivo:
        archivo.write(f"{hash}\n")

def leer_archivo_contras():
    """
    Lee los hash desde archivo y los añade a la lista de los ya agregados.

    """
    with open(os.path.join(ruta_destino, "contras.txt"), "r") as archivo:
        for line in archivo:
            contras_ya_vistas.append(line)

def get_hash(input_string):
    """
    Compute the SHA-384 hash of the input string.
    If there is an error during the computation, return None.
    :param input_string: The string to be hashed
    :return: The computed hash (as a hexadecimal string) or None if an error occurs
    """
    try:
        return hashlib.sha384(input_string.encode()).hexdigest()
    except:
        return None

def recorrer_directorio(ruta_directorio):
    """
    Recursively traverse the directory and its subdirectories, processing files with certain extensions.
    :param ruta_directorio: The path to the root directory
    """
    contras_file_path = os.path.join(ruta_destino, "contras.txt")
    with open(contras_file_path, "a+", encoding="latin1") as contras_file:
        for root, dirs, files in os.walk(ruta_directorio):
            try:
                for file in files:
                    if not file.endswith(tuple(extensiones_excluidas)):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r", encoding="latin1") as archivo:                            
                            for line in archivo:                                
                                if line not in contras_ya_vistas:
                                    contras_ya_vistas.append(line)                                
                                    contras_file.write(line)
                                    #print(line)
                                else:
                                    print(f"{line} ya existe")
                    os.remove(file_path)           
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                pass
if __name__ == "__main__":
    if not os.path.exists(os.path.join(ruta_destino, "contras.txt")):
        open(os.path.join(ruta_destino, "contras.txt"), "w").close()
    leer_archivo_contras()
    recorrer_directorio(ruta_origen)
    print("Proceso terminado")