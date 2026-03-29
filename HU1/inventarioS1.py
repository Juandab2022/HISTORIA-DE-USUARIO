# Programa de inventario simple

print("SISTEMA DE INVENTARIO SIMPLE\n")

# Solicitar nombre del producto
nombre = input("Ingrese el nombre del producto: ")

while nombre=="":
	print("ERROR: debe ingresar el nombre del producto")
	nombre=input("Por Favor ingrese el nombre del producto: ")
	
# Solicitar precio del producto
precio = float(input("Ingrese el precio del producto: "))

while precio<= 0:
	print("ERROR: el precio debe ser mayor de 0")
	precio=float(input("Por Favor ingrese el precio del producto: "))

# Solicitar cantidad
cantidad = int(input("Ingrese la cantidad del producto: "))

while cantidad<= 0:
	print("ERROR: la cantidad debe ser mayor de 0")
	cantidad=int(input("Por Favor ingrese la cantidad de productos que desea llevar: "))

# Calcular costo total
costo_total = precio * cantidad

# Mostrar resultados
print("Producto:", nombre,"\n" "| Precio:", precio, "| Cantidad:", cantidad, "| Costo Total:", costo_total)
print("GRACIAS POR SU COMPRA!!")

# Este programa permite registrar un producto en un inventario simple.
#Hacer la validacion de datos , para que si el usuario si llega a escribir alguna palabra o número mal, aparezca un mensaje de error y tenga la oportunidad de volver a pedir.
# Calcula el costo total multiplicando el precio por la cantidad.
