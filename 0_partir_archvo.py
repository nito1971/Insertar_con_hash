import os
import shutil

# Rutas de las carpetas origen y destino
origin_dir = '/mnt/local/datos/Contras/archivos_no_partidos'
partidos_dir = '/mnt/local/datos/Contras/archivos_partidos'

# Tamaño de cada archivo (1 MB)
chunk_size = 1024

# Recorrer directorio origen y dividir archivos en chunk_size
for file in os.listdir(origin_dir):
    filepath = os.path.join(origin_dir, file)
    
    if os.path.isfile(filepath):  # Si es un archivo
        with open(filepath, 'rb') as f:
            file_contents = f.read()
        
        chunks = [file_contents[i:i + chunk_size] for i in range(0, len(file_contents), chunk_size)]
        
        for i, chunk in enumerate(chunks):
            filename = f"{file}.{i+1}.bin"
            with open(os.path.join(partidos_dir, filename), 'wb') as f:
                f.write(chunk)