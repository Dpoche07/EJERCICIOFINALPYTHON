def ingresar_datos(nota):
    if nota_final >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
    return nota

nombre_aprendiz = input("Escriba su nombre: ")
asignatura = input("Escriba su asignatura: ")
nota_final = int(float(input("Digite su nota: ")))

ingresar_datos(nota_final)