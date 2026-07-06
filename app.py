# SISTEMA DE REGISTRO DE PRODUCTOS #
import os

# Borrar pantalla
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Mostrar menu
def mostrar_menu():
    print("")
    print(f''' {"=== MENU PRINCIPAL ===":^30}

1. Stock por categoria
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
''')

# Leer opcion menu
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("La opcion ingresada no existe.")
        except ValueError:
            print("Error: ingrese un numero entero positivo")