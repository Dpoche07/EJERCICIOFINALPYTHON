import os

opcion = ""

def importe_fila(opcion):
    nombre_fila = f"punto{opcion}.py"
    if os.path.exists(nombre_fila):
        exec(open(nombre_fila).read())
    else:
        print(f"{nombre_fila} no existe.")

while opcion != "salir":
    opcion = input("Elige un punto para ejecuar (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 salir): ")
    if opcion == "salir":
        break
    importe_fila(opcion)