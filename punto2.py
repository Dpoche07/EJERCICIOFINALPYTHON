def numeros_impares(inicio, fin):
    for numero in range(inicio, fin +1):
        if numero % 2 !=0:
            print(numero)
inicio = int(input("digita valor incial: "))
fin = int(input("digita el valor final: "))

if inicio > fin:
    print("el valor inicial deber ser mayor al valor final: ")
else:
    numeros_impares(inicio, fin)


