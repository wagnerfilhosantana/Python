class Produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    @property

    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('Camisa', 50)
p2 = Produto('Short', 'R$24')
p1.desconto(10)
p2.desconto(20)
print(p1.preco)
print(p2.preco)