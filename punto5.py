total_notas = 0
contador_notas = 0
cantidad_notas = int(input("Notas a ingresar: "))
while contador_notas < cantidad_notas:
    nota = float(input(f"ingresa la nota {contador_notas + 1} (entre 0 y 5.0):"))
    if 0 <= nota <= 5.0:
        total_notas += nota
        contador_notas += 1
    else:
        print("la nota no es valida, debe estar entre 0 y 5.0")
promedio = total_notas / cantidad_notas
print(f"\nPromedio de notas: {promedio:.2f}")
if promedio >= 4.5:
    print("APROBADO")
else:
    print("NO APROBADO")