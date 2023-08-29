class Conta():
    def __init__(self, pessoa, saldo):
        self.pessoa = pessoa
        self.saldo = saldo
        
    def verSaldo(self):
        print(f'Olá, {self.pessoa}! O seu saldo inicial é de: R$ {self.saldo}.')
        
    def depositar(self):
        valor = float(input('Qual o valor a ser depositado? '))
        self.saldo = self.saldo + valor
        print(f'Voce depositou R$ {valor}.')
        
    def sacar(self):
        valor = float(input('Qual o valor a ser sacado? '))
        self.saldo = self.saldo - valor
        print(f'Voce sacou R$ {valor}.')
        print(f'Seu saldo é de: R$ {self.saldo}')
        
saldo = Conta('Gustavo', 200)

saldo.verSaldo()
saldo.depositar()
saldo.sacar()

