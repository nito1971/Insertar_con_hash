import os
import hashlib

## Define the origin directory and the destination directory for writing output files.
ruta_origen = "/mnt/10.0.1.20/datos/Contras/Sin_procesar"
ruta_destino = "/mnt/10.0.1.20/datos/Contras/procesado"

## Define a list of file extensions to exclude from processing
extensiones_excluidas = ["sql", "xlxs", "docx", "doc", "html"]
hashes = []  # Initialize an empty list for storing hashes

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
    contras_file_path = os.path.join(ruta_destino, "Collection_1.txt")
    with open(contras_file_path, "a+", encoding="latin1") as contras_file:
        for root, dirs, files in os.walk(ruta_directorio):
            try:
                for file in files:
                    if not file.endswith(tuple(extensiones_excluidas)):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r", encoding="latin1") as archivo:
                            lines = archivo.readlines()
                            for line in lines:
                                hashed_line = get_hash(line.decode())
                                if hashed_line not in hashes:
                                    hashes.append(hashed_line)
                                    contras_file.write(f"{hashed_line}\n")
                                    print(hashed_line)  #
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")