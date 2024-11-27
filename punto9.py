def calcular_calificacion_final():

  nombre = input("Ingrese el nombre del estudiante: ")
  asignatura = input("Ingrese el nombre de la asignatura: ")

  nota1 = float(input("Ingrese la nota del primer examen (0-5): "))
  nota2 = float(input("Ingrese la nota del segundo examen (0-5): "))
  nota3 = float(input("Ingrese la nota del tercer examen (0-5): "))

  while nota1 < 0 or nota1 > 5 or nota2 < 0 or nota2 > 5 or nota3 < 0 or nota3 > 5:
    print("Las notas deben estar entre 0 y 5. Por favor, ingrese las notas nuevamente.")
    nota1 = float(input("Ingrese la nota del primer examen (0 y 5): "))
    nota2 = float(input("Ingrese la nota del segundo examen (0 y 5): "))
    nota3 = float(input("Ingrese la nota del tercer examen (0 y 5): "))

  calificacion_final = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4

  if calificacion_final >= 4.0:
    resultado = "APROBADO"
  else:
    resultado = "REPROBADO"

  print(f"\nEstudiante: {nombre}")
  print(f"Asignatura: {asignatura}")
  print(f"Calificación final: {calificacion_final:.2f}")
  print(f"Resultado: {resultado}")

calcular_calificacion_final()