import os
import shutil

'''
Este script utiliza la biblioteca os para interactuar c
on el sistema de archivos y la biblioteca shutil para copiar archivos. 
a función split_file toma un archivo como entrada y
lo divide en partes de 1000 líneas, guardando cada parte en un archivo
separado en la ruta especificada.

Luego, el script recorre la carpeta principal y llama a la 
función split_file para cada archivo que encuentra. 
Cada archivo partido se almacena en la ruta específica
con la extensión .txt.
'''

# Ruta principal
root_dir = "/mnt/local/datos/Contras/archivos_no_partidos"

# Ruta donde se almacenarán los archivos partidos
parted_dir = "/mnt/local/datos/Contras/archivos_partidos"

# Función para dividir un archivo en partes de 1000 líneas
def split_file(file_path, output_dir):
    with open(file_path, 'r', encoding="latin1") as file:
        lines = [line.strip() for line in file.readlines()]
        num_parts = -(-len(lines) // 1000)
        part_size = len(lines) // num_parts

        for i in range(num_parts):
            start_idx = i * part_size
            end_idx = (i + 1) * part_size
            if i == num_parts - 1:
                end_idx = len(lines)

            with open(os.path.join(output_dir, f"part-{i+1}.txt"), 'a+', encoding="latin1") as part_file:
                part_file.write('\n'.join(lines[start_idx:end_idx]))

# Recorrer la carpeta y dividir los archivos
for file in os.listdir(root_dir):
    file_path = os.path.join(root_dir, file)
    if os.path.isfile(file_path):
        split_file(file_path, parted_dir)