import os
carros = []

class Carros:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velMax = int(potencia * 2)
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def deligar(self):
        self.ligado = False

    def info(self):
        print(f'Nome......: {self.nome}')
        print(f'Potencia..: {self.potencia}')
        print(f'Vel.Maxima: {self.velMax}')
        print(f'Ligado....: {"sim" if self.ligado == True else "nao"}')

def menu():
    os.system('cls') or None
    print("1 - Novo Carro")   
    print("2 - informacoes do carro")  
    print("3 - Excluir carro")  
    print("4 - Ligar Carro")  
    print("5 - Desligar Carro")  
    print("6 - Listar  Carros")  
    print("7 - Sair")  
    print(f'Quantidade de carros: {str(len(carros))}')
    opcao = input('Digite uma opcao: ')
    return opcao
def NovoCarro():
    os.system('cls') or None
    nom = input('Nome do Carro:')
    pot = int(input('Potencia: '))
    car = Carros(nom, pot)
    carros.append(car)
    print('Novo carro criado!')
    os.system('pause')

def informacoes():
    os.system('cls') or None
    NumCarro = input('Digite o numero do que deseja ver as informacoes: ')
    try:
        carros[int(NumCarro)].info()

    except:
        print('O carro nao existe na lista!')
    os.system('pause')

def Excluir():
    os.system('cls') or None
    NumCarro = input('Digite o numero do que deseja Excluir: ')
    try:
        del carros[int(NumCarro)]

    except:
        print('O carro nao existe na lista!')
    os.system('pause')

def Ligar():
    os.system('cls') or None
    NumCarro = input('Digite o numero do que deseja ligar: ')
    try:
        carros[int(NumCarro)].ligar()

    except:
        print('O carro nao existe na lista!')
    os.system('pause')

def Desligar():
    os.system('cls') or None
    NumCarro = input('Digite o numero do que deseja ver as desligar: ')
    try:
        carros[int(NumCarro)].desligar()

    except:
        print('O carro nao existe na lista!')
    os.system('pause')

def Lista_carro():
    os.system('cls') or None
    p = 0
    for contador in carros:
        print((str(p) + "-" + contador.nome))
        p += 1
    os.system('pause')

repeat = menu()

while repeat < '7':
    if repeat == '1':
        NovoCarro()
    elif repeat == '2':
        informacoes()
    elif repeat == '3':
        Excluir()
    elif repeat == '4':
        Ligar()
    elif repeat == '5':
        Desligar()
    elif repeat == '6':
        Lista_carro()
    repeat = menu()

os.system('cls') or None
print('fim do programa!')