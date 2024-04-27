import os
import rarfile

def extract_rar_files(directory):
    for root, dirs, files in os.walk(directory):
        # Recorre los archivos en el directorio
        for file in files:
            try:
                # Verifica si el archivo es un RAR
                if file.endswith(".rar"):
                    full_path = os.path.join(root, file)
                    print(f"Descomprimiendo {full_path}...")
                    rarfile.RarFile(full_path).extractall(os.path.dirname(full_path))
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                pass

# Utiliza el script
directory = "/mnt/10.0.1.20/datos/Contras/Sin_procesar"
extract_rar_files(directory)