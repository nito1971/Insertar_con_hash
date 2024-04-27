import os
origen_datos = "/mnt/10.0.1.20/datos/Contras/procesado/contras.txt"

lista_cadenas_encontradas = []
def encontrar_texto(archivo, texto):
    
    with open(archivo, "r", encoding="latin1") as f:
        for linea in f:
            if texto in linea:
                lista_cadenas_encontradas.append(linea)
            else:
                continue
    with open("resultado.txt", "a+", encoding="latin1") as f:
        for linea in lista_cadenas_encontradas:
            f.write(linea)
    return lista_cadenas_encontradas
        
    


def menu():
        while True:
            if os.path.exists("resultado.txt"):
                os.remove("resultado.txt")
            print("\nMenu:")
            print("1. Buscar cadena")
            print("2. Salir")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                cadena = input("Introduce la cadena a buscar: ")
                encontrar_texto(origen_datos,cadena)
                for linea in encontrar_texto(origen_datos, cadena):
                    print(linea)
            elif opcion == "2":
                print("\nSaliendo...")
                break
            else:
                print("\nOpción inválida. Vuelva a intentar.")

if __name__ == "__main__":
    menu()