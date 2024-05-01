import os
import glob
contador_archivos = 0
contador_linas = 0
nombre_archivo = 0
limite_lineas = 2
lineas = []
archivos = []
ruta = "/mnt/local/datos/Contras/archivos_partidos"
directorio_donde_buscar = "/mnt/local/datos/Contras/archivos_no_partidos"


def obtener_archivos(directorio_donde_buscar):
    for archivo in glob.iglob(f'{directorio_donde_buscar}/**/*', recursive=True):
        if os.path.isfile(archivo):
            archivos.append(archivo)
    return archivos


archivos_final = obtener_archivos(directorio_donde_buscar)



for archivo in archivos_final:
    limite_lineas = 100
    try:        
        with open(archivo, encoding="latin-1") as f:
            for linea in f:
                if contador_linas < limite_lineas:
                    lineas.append(linea)
                    contador_linas += 1
                elif contador_linas == limite_lineas:
                    nombre_archivo += 1
                    with open(f"{ruta}/305{contador_archivos}.txt", "w") as f2:
                        f2.writelines(lineas)
                        lineas = []
                        contador_linas = 0
                        contador_archivos += 1
    except Exception as e:
        print(e)
        pass


