lista = []

while True:
    print("O que você quer fazer? \n".upper())
    print("1, Adicionar tarefa")
    print("2, Executar tarefa")
    print("3, Sair\n")
    
    op = int(input("Digite sua opção: "))
    
    if op == 1:
        tarefa = input("Descreva sua tarefa: ")
        lista.append(tarefa)
        
    elif op == 2:
        print(f"Executando: {lista.pop(0)}")
        
    else:
        print("Saindo...")
            