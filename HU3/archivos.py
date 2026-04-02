
import csv


def guardar_csv(inventario, ruta, incluir_header=True):  #Guardar el inventario en un archivo CSV

    if not inventario:      #Verifica que haya datos antes de guardar
        print("No hay productos para guardar.")
        return

    try:

        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for producto in inventario: #Recorre el inventario y escribe cada producto 

                writer.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta): #Carga el inventario desde un archivo CSV

    inventario = []

    errores = 0

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:

            reader = csv.reader(archivo)

            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                raise ValueError("Encabezado inválido")

            for fila in reader:

                try:

                    if len(fila) != 3:
                        raise ValueError

                    nombre = fila[0]

                    precio = float(fila[1])

                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                   #agrega el producto válido al inventario 
                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"{errores} filas inválidas omitidas")

        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")

    except UnicodeDecodeError:
        print("Error de codificación")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Error inesperado:", e)

    return []