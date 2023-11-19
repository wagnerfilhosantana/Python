from random import randint

class Pessoa:
    ano_atual = 2023
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls,nome, ano_nascimento):
        idade = cls.ano_atual - cls.ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_num():
        rand = randint(10000, 99999)
        return rand
    

p1 = Pessoa('Wagner', 23)
print(f'Ola {p1.nome}, voce tem {p1.idade}')
p1.get_nascimento()
print(p1.gera_num())