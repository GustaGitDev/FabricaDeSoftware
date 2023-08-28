sexo = ""
homen = 0
mulher = 0
while sexo != "sair":
    sexo = input("Diga o sexo: ").lower()
    
    if sexo == "h":
        homen = homen + 1
    elif sexo == "m":
        mulher = mulher + 1
print(f"A quantidade de homens eh: {homen} e a quantidade de mulheres eh: {mulher}.")    