'''
Script que recorre distintos tipos de ficheros y
extrae su contenido y lo inserta en un archivo evitando duplicados.
El archivo de salida es un archivo txt.
'''

import os
import hashlib

## Define the origin directory and the destination directory for writing output files.
ruta_origen = "/mnt/10.0.1.20/datos/Contras/TXT"
ruta_destino = "/mnt/10.0.1.20/datos/Contras/terminado"

## Define a list of file extensions to exclude from processing
extensiones_excluidas = ["sql", "xlxs", "docx", "doc", "html", "rar"]
contras_ya_vistas  = []  # Initialize an empty list for storing hashes

def leer_archivo_contras():
    """
    Lee los hash desde archivo y los añade a la lista de los ya agregados.

    """
    with open(os.path.join(ruta_destino, "contras.txt"), "r") as archivo:
        for line in archivo:
            contras_ya_vistas.append(line)

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
                                    print(line)                                                              
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