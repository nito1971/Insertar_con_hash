import os
import random
import glob
contador_linas = 0
nombre_archivo = 0
limite_lineas = 2
lineas = []
archivos = []
directorio_donde_guardar = "/mnt/10.0.1.20/datos/Contras/listo"
directorio_donde_buscar = "/mnt/10.0.1.20/datos/Contras/procesado"

def generar_limite_lineas():
    limite = random.randint(1999, 2000)
    return limite

def generar_randon():
    intervalo = random.randint(10000, 10000000000000)
    return intervalo

'''
def obtener_archivos(directorio_donde_buscar):
    for archivo in glob.iglob(f'{directorio_donde_buscar}/**/*', recursive=True):
        if os.path.isfile(archivo):
            archivos.append(archivo)
    return archivos

'''
def obtener_archivos(directorio_donde_buscar):
    for root, dirs, files in os.walk(directorio_donde_buscar):
        try:
             for file in files: 
                file_path = os.path.join(root, file)
                archivos.append(file_path) 
                return archivos                                  
        except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
                    pass


archivos_final = obtener_archivos(directorio_donde_buscar)



for archivo in archivos_final:
    limite_lineas = generar_limite_lineas()
    try:        
        with open(archivo, encoding="latin-1") as f:
            try:
                for linea in f:
                    if contador_linas < limite_lineas:
                        lineas.append(linea)
                        contador_linas += 1
                    elif contador_linas == limite_lineas:
                        nombre_archivo += 1
                        with open(f"{directorio_donde_guardar}/+{nombre_archivo}{generar_randon()}{generar_randon()}{generar_randon()}{generar_randon()}{generar_randon()}{generar_randon()}.txt", "w") as f2:
                            f2.writelines(lineas)
                            lineas = []
                            contador_linas = 0
            except Exception as e:
                print(e)
                pass    
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

