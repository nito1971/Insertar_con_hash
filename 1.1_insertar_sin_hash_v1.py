'''
Script que recorre distintos tipos de ficheros y
extrae su contenido y lo inserta en un archivo evitando duplicados.
El archivo de salida es un archivo txt.
'''

import os
import time

## Define the origin directory and the destination directory for writing output files.
ruta_origen = "/mnt/local/datos/ALIMENTACION_PROYECTOS/EMAIL/partido"
ruta_destino = "/mnt/local/datos/Contras/listo"

## Define a list of file extensions to exclude from processing
extensiones_excluidas = ["sql", "xlxs", "docx", "doc", "html", "rar"]
contras_ya_vistas  = []  # Initialize an empty list for storing hashes

def leer_archivo_contras():
    """
    Lee las lineas desde archivo y los añade a la lista de las ya agregados.

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
                        incio = time.time()
                        with open(file_path, "r", encoding="latin1") as archivo:                            
                            for line in archivo: 
                                if line.split("/n") not in contras_ya_vistas:
                                    line = line
                                    contras_ya_vistas.append(line)                                
                                    #print(line
                                    contras_file.write(line)
                                    #print(line)  
                                else:
                                    print(f"{line} ya existe")
                        if os.path.exists(file_path):                                                            
                            os.remove(file_path) 
                            fin = time.time()
                            print(f"Archivo {file_path} eliminado")  
                            tiempo = fin - incio
                            print(f"Tiempo de ejecucion: {tiempo} segundos")        
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                pass
   

# Main Script
if __name__ == "__main__":
    # Create or open "contras.txt" file if it doesn't exist
    contras_file_path = os.path.join(ruta_destino, "contras.txt")
    if not os.path.exists(contras_file_path):
        with open(contras_file_path, 'w') as f:
            pass
    
    # Log the start of processing
    print("Leyendo archivo contras.txt")
    
    # Read the file and process it
    leer_archivo_contras()
    print("Archivo leido")
    
    # Start processing the directory
    print("Procesando directorio")
    recorrer_directorio(ruta_origen)
    print("Proceso terminado")