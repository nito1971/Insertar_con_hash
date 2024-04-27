import os
import zipfile

def extract_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                full_path = os.path.join(root, file)
                print(f"Descomprimiendo {full_path}...")
                with zipfile.ZipFile(full_path, 'r') as zip_file:
                    zip_file.extractall(os.path.dirname(full_path))

# Utiliza el script
directory = "/mnt/10.0.1.20/datos/Contras/Sin_procesar"
extract_zip_files(directory)