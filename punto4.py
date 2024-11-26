def calcular_inversion():
    try:
        capital_inicial = float(input("ingresa la cantidad de dinero a invertir: "))
        interes_anual = float(input("ingresa el interes anual (en %): "))
        tiempo = int(input("digita el numero de años: "))
        capital_final = capital_inicial * (1 + interes_anual / 100)** tiempo

        print(f"\n despues de {tiempo} años su inversión será de ${capital_final:.2f}")
    except ValueError:
        print("por favor, ingresa valores numéricos validos")
if __name__ == "__main__":
    calcular_inversion()