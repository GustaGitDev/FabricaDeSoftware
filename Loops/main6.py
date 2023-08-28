cont = 0
while True:
    num = int(input("Digite um numero: "))
    cont += num
    if num == 0:
        break
    else:
        continue
print(cont)    