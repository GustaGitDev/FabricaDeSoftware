num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais outro numero: "))

if num1 > num2 and num1 > num3:
    print("{} eh maior que {} e {}.".format(num1, num2, num3))
    
    if num2 < num3:
        print("{} eh o menor numero.".format(num2))
    else:
        print("{} eh o menor numero.".format(num3))
    
elif num2 > num1 and num2 > num3:
    print("{} eh maior que {} e {}.".format(num2, num1, num3))
    
    if num1 < num3:
        print("{} eh o menor numero.".format(num1))
    else:
        print("{} eh o menor numero.".format(num3))
    
elif num3 > num2 and num3 > num1:
    print("{} eh maior que {} e {}.".format(num3, num2, num1))
    
    if num2 < num1:
        print("{} eh o menor numero.".format(num2))
    else:
        print("{} eh o menor numero.".format(num1))