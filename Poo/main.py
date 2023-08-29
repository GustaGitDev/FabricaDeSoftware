class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca
        
    def __str__(self):
        return f"Oi, eu sou uma garrafa da {self.marca}"
    
    def __eq__(self, obj):
        if self.marca == obj.marca:
            return True
        else:
            return False
        
garrafa = Garrafa(100, 'preto', 'shopee')
stanley = Garrafa(100, 'preto', 'stanley')
print(garrafa)
print(stanley)
print(garrafa == stanley)