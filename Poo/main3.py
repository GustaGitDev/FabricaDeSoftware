class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def acelerar (self):
        print(f'Seu carro da marca {self.marca}, do modelo {self.modelo} e do ano {self.ano}, esta ACELERANDO...')
        
carro = Carro('Ford', 'Mustang', 2005)    

carro.acelerar() 