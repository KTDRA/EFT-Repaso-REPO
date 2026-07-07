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

# ========== FUNCIONES DE VALIDACION Y CONTROL ==========

# Nombre
def validar_texto(texto):
    return texto.strip() != ""

# Entero positivo mayor a 0
def validar_entero_positivo(precio):
    return precio > 0

# Entero positivo o 0
def validar_entero(stock):
    return stock >= 0

# Disponibilidad
def validar_disponible(opcion):
    opcion = opcion.lower()
    return opcion == "s" or opcion == "n"

# Buscar codigo
def buscar_codigo(productos, codigo):
    codigo = codigo.upper().strip()
    if codigo in productos:
        return True
    return False

# validar codigo
def validar_codigo(productos, codigo):
    codigo = codigo.upper().strip()
    if validar_texto(codigo) and codigo not in productos:
        return True
    return False

# Leer entero
def leer_entero(mensaje):
    while True:
        try:
            entero = int(input(mensaje))
            return entero
        except ValueError:
            print("Ingresa un numero entero")

# ========== FUNCIONES DE CONTROL =========

# Leer texto no vacio
def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje)
        if validar_texto(texto):
            return texto
        else:
            print("El campo no puede estar vacio")

# ========== FUNCIONES EJECUTIVAS DE OPCIONES DEL MENU =========
