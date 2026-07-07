# SISTEMA DE REGISTRO DE PRODUCTOS #
#
# inventario = {codigo:[stock,vendidos]}

# productos = {codigo:[nombre,categoria,precio,disponible]}
#
#
#
#
#
#
#

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

# ========== FUNCIONES LOGICAS ASISTENTES DE OPCIONES DEL MENU =========

# Agregar producto
def agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario):
    if not validar_codigo(productos,codigo):
        return False
    if disponible.lower().strip() == "s":
        disponible_bool = True
    else:
        disponible_bool = False
    
    productos[codigo] = [nombre,categoria,precio,disponible_bool]

    inventario[codigo] = [stock,vendidos]

    return True

# Stock por categoria
def stock_categoria(categoria, productos,inventario):
    categoria = categoria.upper().strip()
    total_stock = 0
    for codigo, datos in productos.items():
        if datos[1] == categoria:
            total_stock += inventario[codigo][0]
    
    return total_stock

# Busqueda por rango de precio
def buscar_precio(precio_min,precio_max,productos,inventario):
    items = []
    if precio_max < precio_min:
        return False
    for codigo in productos:
        if (precio_min <= productos[codigo][2] <= precio_max) and inventario[codigo][0] > 0:
            item = [productos[codigo][1],productos[codigo][2]]
            items.append(item)
    return items

# Actualizar precio
def actualizar_precio(codigo,nuevo_precio,productos):
    codigo = codigo.upper().strip()
    if buscar_codigo(productos,codigo):
        productos[codigo][2] = nuevo_precio
        return True
    return False

# Eliminar producto
def eliminar_producto(codigo, productos,inventario):
    codigo = codigo.upper().strip()
    if buscar_codigo(productos,codigo):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False