#lista donde se almacenaran todos los productos
inventario = []

#FUNCIONES
#======================

#función para agegar un producto al inventario
def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

#crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
#agregar producto a la lista
    inventario.append(producto)
    print("Producto agregado correctamente")

#función para mostrar todos los productos 
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío")
    else:
        print("\nInventario:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

#función para calcular estadísticas
def calcular_estadisticas():
    if not inventario:
        print("No hay datos para calcular")
        return

    total_valor = 0
    total_cantidad = 0

#recorrer inventario y calcular valores
    for producto in inventario:
        total_valor += producto["precio"] * producto["cantidad"]
        total_cantidad += producto["cantidad"]

    print(f"\nValor total del inventario: {total_valor}")
    print(f"Cantidad total de productos: {total_cantidad}")



#MENÚ PRINCIPAL
# ======================
#variable para el contol del programa
ejecutando = True

while ejecutando:
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa...")
        ejecutando = False
    else:
        print("Opción inválida, intenta de nuevo")
        
        
#COMENTARIO FINAL:
"""En este proyecto desarollé un programa en python que permite gestionar un inventario utilizando listas
y diccionarios. Incluye un menú interactivo, que permite agregar productos, mostrarlos y calcular estadistíscas básicas.""" 
