def calcular():
    def soma (num1, num2):
        return num1 + num2

    def div (num1, num2):
        return num1 / num2

    def mult (num1, num2):
        return num1 * num2

    def sub (num1, num2):
        return num1 - num2

    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    command = str(input("Qual operacao voce quer fazer? ")).lower()

    if command == 'soma':
        print(soma(num1, num2))
    elif command == 'mult':
        print(mult(num1, num2))
    elif command == 'div':
        print(div(num1, num2))   
    elif command == 'sub':
        print(sub(num1, num2))
    else:
        print("comando não reconhecido.")
        
    