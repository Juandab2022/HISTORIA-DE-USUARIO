from funciones import *
from archivos import *

inventario = [] #lista principal donde se guardan los productos
control = True

while control: #bucle principal del programa 

    print("\n--- MENÚ INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Seleccione opción: ")

    try:

        if opcion == "1":
            nombre = input("Nombre: ").strip() #elimina espacios extras 

            #Validación del precio
            precio_valido = False
            while not precio_valido:
                try:
                    precio = float(input("Precio: "))
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        precio_valido = True
                except ValueError:
                    print(" ingresa un número válido.")

            #Validación de la cantidad 
            cantidad_valida = False
            while not cantidad_valida:
                try:
                    cantidad = int(input("Cantidad: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                    else:
                        cantidad_valida = True
                except ValueError:
                    print("Debe ingresar un número entero.")

           #llama a la función para agregar el producto
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario) #muestra todos los productos 

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            print(producto if producto else "No encontrado")

        elif opcion == "4":
            nombre = input("Producto a actualizar: ")

            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad: "))

            actualizar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "5":
            nombre = input("Producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print(stats)

        elif opcion == "7":
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta archivo: ")
            datos = cargar_csv(ruta)

            if datos:
                decision = input("¿Sobrescribir inventario? (S/N): ")

                if decision.upper() == "S":
                    inventario = datos
                else:
                    for p in datos:
                        existente = buscar_producto(inventario, p["nombre"])

                        if existente:
                            existente["cantidad"] += p["cantidad"]
                            existente["precio"] = p["precio"]
                        else:
                            inventario.append(p)

        elif opcion == "9":
            print("Programa finalizado")
            control = False

        else:
            print("Opción inválida")

    except Exception as e: #evita que el programa se cierre por errores 
        print("Error:", e)