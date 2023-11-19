class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.classenome = self.__class__.__name__

    def falar(self):
        print (f'{self.classenome} esta falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.classenome} esta comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.classenome} esta estudando...')