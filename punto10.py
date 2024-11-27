def calcular_descuento(precio):
    if precio > 20000:
        descuento = precio * 0.20
        precio_con_descuento = precio - descuento
        return precio_con_descuento
    else:
        return precio
precio = int(float(input("Digite el precio: $")))
precio_a_pagar = calcular_descuento(precio)
print(f"El valor a pagar es: $ {precio_a_pagar:.2f}")
    