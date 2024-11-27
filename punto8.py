def jubilación(edad, sexo):
    if edad > 54 and sexo == "F":
        print("Esta mujer se puede jubilar")
    elif edad >= 63 and sexo =="M":
        print("Este hombre se puede jubilar")
    else:
        print("No se puede jubiliar :C")
    return

edad = int(input("Digite la edad:"))
sexo = input("Digite el sexo: ")

jubilación(edad, sexo)