class Animal():
    def __init__(self, nome):
        self.nome = nome
    def info(self):
        print(f'Sou um {self.nome}.')
        
class Gato(Animal):
    def som(self):
        print('Miado')
    
class Cachorro(Animal):
    def som(self):
        print('Latido')
        
cachorro = Cachorro("Cachorro")
gato = Gato("Gato")

cachorro.info()
cachorro.som()
gato.info()
gato.som()
