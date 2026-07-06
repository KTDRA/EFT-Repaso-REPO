# SISTEMA DE REGISTRO DE PRODUCTOS #
import os

# Borrar pantalla
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ========== FUNCIONES DEL MENU ============

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
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Error: ingrese un numero entero positivo")

# ========== FUNCIONES DE VALIDACION ==========

# Nombre
def validar_nombre(nombre):
    return nombre.strip() != ""

# Categoria
def validar_categoria(categoria):
    return categoria.strip() != ""

# Precio
def validar_precio(precio):
    return precio > 0

# Stock
def validar_stock(stock):
    return stock >= 0

# Productos vendidos
def validar_vendidos(vendidos):
    return vendidos >= 0

# Disponibilidad
def validar_disponible(opcion):
    opcion = opcion.lower()
    return opcion == "s" or opcion == "n"