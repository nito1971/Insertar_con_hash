import os
import random
import glob
contador_linas = 0
nombre_archivo = 0
limite_lineas = 2
lineas = []
archivos = []
ruta = "/mnt/local/datos/ALIMENTACION_PROYECTOS/EMAIL/cifrado"
directorio_donde_buscar = "/mnt/local/datos/ALIMENTACION_PROYECTOS/EMAIL/original"

def generar_limite_lineas():
    limite = random.randint(2, 1000)
    return limite

def generar_randon():
    intervalo = random.randint(10000, 10000000000000)
    return intervalo
def obtener_archivos(directorio_donde_buscar):
    for archivo in glob.iglob(f'{directorio_donde_buscar}/**/*', recursive=True):
        if os.path.isfile(archivo):
            archivos.append(archivo)
    return archivos


archivos_final = obtener_archivos(directorio_donde_buscar)



for archivo in archivos_final:
    limite_lineas = generar_limite_lineas()
    try:        
        with open(archivo, encoding="latin-1") as f:
            for linea in f:
                if contador_linas < limite_lineas:
                    lineas.append(linea)
                    contador_linas += 1
                elif contador_linas == limite_lineas:
                    nombre_archivo += 1
                    with open(f"{ruta}/+{nombre_archivo}{generar_randon()}{generar_randon()}{generar_randon()}{generar_randon()}.txt", "w") as f2:
                        f2.writelines(lineas)
                        lineas = []
                        contador_linas = 0
    except Exception as e:
        print(e)
        pass







                
            
'''

with open("./original/j", encoding="latin-1") as f:
    for linea in f:
        if contador_linas < limite_lineas:
            lineas.append(linea)
            contador_linas += 1
        elif contador_linas == limite_lineas:
            nombre_archivo += 1
            with open(f"./partido/j_{nombre_archivo}.txt", "w") as f2:
                f2.writelines(lineas)
                lineas = []
                contador_linas = 0

'''

