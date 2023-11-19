class CarrinhoDecompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produtos(self,produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, ':', produto.valor, 'reais')

    def total_produto(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
        
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
