def convertir_dolares_a_pesos(dolares, tasa_cambio):
    return dolares * tasa_cambio

def main():
    tasa_cambio = 3934
    continuar = True

    print("conversión de dólares a pesos.")
    while continuar:
        try:
            dolares = float(input("Ingrese la cantidad en dólares: "))
            if dolares < 0:
                print("Por favor, ingrese un valor positivo.")
                continue

            pesos = convertir_dolares_a_pesos(dolares, tasa_cambio)
            print(f"{dolares} dólares equivalen a {pesos:,.2f} pesos.")
        except ValueError:
            print("Valor inválido. Por favor ingrese un número válido.")
            continue

        respuesta = input("¿Desea realizar otra conversión? (s/n): ").strip().lower()
        if respuesta != 's':
            continuar = False
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")

if __name__ == "__main__":
    main()
