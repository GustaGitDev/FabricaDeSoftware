azul = int(input("Quantidade de canetas azuis: "))
preta = int(input("Quantidade de canetas pretas: "))

valAzul = azul * 2
valPreta = preta * 2.5

valorFinal = valAzul + valPreta

print("O valor final a ser pago eh de: R$ {}.".format(valorFinal))