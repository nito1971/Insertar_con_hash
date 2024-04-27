import os
import hashlib

## Define the origin directory and the destination directory for writing output files.
ruta_origen = "/mnt/10.0.1.20/datos/Contras/Sin_procesar"
ruta_destino = "/mnt/10.0.1.20/datos/Contras/procesado"

## Define a list of file extensions to exclude from processing
extensiones_excluidas = ["sql", "xlxs", "docx", "doc", "html"]
hashes = []  # Initialize an empty list for storing hashes

def insertar_en_archivo_hash(hash):
    """
    Write the hash to a file.
    :param hash: The hash to be written
    """
    with open(os.join(ruta_destino, "hashes.txt"), "a") as archivo:
        archivo.write(f"{hash}\n")

def leer_archivo_hash():
    """
    Write the hash to a file.
    :param hash: The hash to be written
    """
    with open(os.join(ruta_destino, "hashes.txt"), "a") as archivo:
        for line in archivo:
            hashes.append(line.strip())

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
                                hashed_line = get_hash(line)
                                if hashed_line not in hashes:
                                    hashes.append(hashed_line)
                                    contras_file.write(f"{line}")
                                    print(line)  #
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                pass
if __name__ == "__main__":
    recorrer_directorio(ruta_origen)
    print("Proceso terminado")