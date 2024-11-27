def saltos_de_linea():
    for i in range(1, 31):
        print(i, end="")
        if i % 7 ==0:
            print("\n", end="")
        print()


saltos_de_linea()