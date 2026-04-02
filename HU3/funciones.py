

def agregar_producto(inventario, nombre, precio, cantidad):
    """

    Agrega un nuevo producto al inventario.
    
    sus parámetros son:
    inventario (list): lista de productos
    nombre (str)
    precio (float)
    cantidad (int)

    """



    producto = {

        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad

    }



    inventario.append(producto)


def mostrar_inventario(inventario): #muestra los productos del inventario 


    if not inventario:

        print("Inventario vacío")

        return


    for producto in inventario:
        print(

            f"Nombre: {producto['nombre']} | "

            f"Precio: {producto['precio']} | "

            f"Cantidad: {producto['cantidad']}"

        )



def buscar_producto(inventario, nombre): #busca un producto por su nombre 

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            return producto


    return None



def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):#actualiza el precio o cantidad de un producto 

    producto = buscar_producto(inventario, nombre)

    if producto is None:

        return False


    if nuevo_precio is not None:

        producto["precio"] = nuevo_precio


    if nueva_cantidad is not None:

        producto["cantidad"] = nueva_cantidad


    return True



def eliminar_producto(inventario, nombre): #elimina un producto del inventario

    producto = buscar_producto(inventario, nombre)


    if producto:

        inventario.remove(producto)

        return True

    return False



def calcular_estadisticas(inventario): #calcula estadísticas del inventario

  
    if not inventario:

        return None



    unidades_totales = sum(p["cantidad"] for p in inventario)



    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)



    producto_mas_caro = max(inventario, key=lambda p: p["precio"])



    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])



    return {

        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock

    }

         #este return se encarga de retornar un diccionario con los resultados
