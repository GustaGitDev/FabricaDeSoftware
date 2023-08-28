velocidade = int(input("Velocidade do carro: "))
passou = velocidade - 80
multa = passou * 7

if velocidade > 80:
    print("Voce sera multado em R$ {}.".format(multa))
else:
    print("Voce nao foi multado")