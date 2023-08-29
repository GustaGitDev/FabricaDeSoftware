class Pessoa():
    def __init__(self, nome, idade, prof):
        self.nome = nome
        self.idade = idade
        self.prof = prof
    def saudacao(self):
        print(f'Oi, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.prof}.')
pedro = Pessoa('Pedro', 25, 'reporter')
pedro.saudacao()

guilherme = Pessoa('Guilherme', 18, 'estudante')
guilherme.saudacao()

ewe = Pessoa('Ewewlyn', 18, 'estudante')
ewe.saudacao()

        
        