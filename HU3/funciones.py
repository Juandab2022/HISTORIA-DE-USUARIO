
#función para agregar productos
def agregar_producto(inventario,nombre,precio,cantidad):
    producto={
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,

    }
    inventario.append(inventario) # sirve para agregar 


def mostrar_inventario(inventario):
    if not inventario:
        print("inventario vacio")
        return
    for producto in inventario:
        print("producto encontrado")



def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower()== nombre.lower():
            return producto
    return None 


def actualizar_producto(inventario,nombre, nuevo_precio=None, nueva_cantidad=None):
    producto= buscar_producto(inventario, nombre)
    if producto is None:
        return False
    
    if nuevo_precio is not None:
        producto= ["precio"]= nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"]= nueva_cantidad

    return True

def eliminar_producto(inventario, nombre):
    producto= buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    

    