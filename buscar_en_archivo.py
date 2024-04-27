import os
origen_datos = "/mnt/10.0.1.20/datos/Contras/procesado/contras.txt"

def encontrar_texto(archivo, texto):
    lista_cadenas_encontradas = []
    with open(archivo, "r", encoding="latin1") as f:
        for linea in f:
            if texto in linea:
                lista_cadenas_encontradas.append(linea)
            else:
                continue
    return lista_cadenas_encontradas
        
    


def menu():
        while True:
            print("\nMenu:")
            print("1. Buscar cadena")
            print("2. Salir")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                cadena = input("Introduce la cadena a buscar: ")
                encontrar_texto(origen_datos,cadena)
                for linea in encontrar_texto("contras.txt", cadena):
                    print(linea)
            elif opcion == "2":
                print("\nSaliendo...")
                break
            else:
                print("\nOpción inválida. Vuelva a intentar.")

if __name__ == "__main__":
    menu()