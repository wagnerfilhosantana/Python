class Carro:
    def __init__(self, consumo, velocidade):
        self.consumo = consumo
        self.velocidade = velocidade
        self.gasolina = 0
        self.ligado = False
        self.desligado = True

    def andar(self, distancia):
        if not self.gasolina <= distancia / self.consumo:
            print('Combustivel suficiente!')
            if self.ligado == True:
                print(f'Seu carro esta andando a {self.velocidade} KM por hora!')
            else:
                print('Voce precisa ligar seu carro primeiro!')
        else:
            print('Combustivel insuficiente!')

    def ligar(self):
        self.ligado = True
        return self.ligado
        
    def desligar(self):
        self.ligado = False
        print('Seu carro esta desligado!')
        return self.ligado
    
    def freio(self, freiar):
        self.velocidade -= freiar
        print(f'Seu carro esta a {self.velocidade} KM por hora!')

    def obterGasolina(self):
        nivel_atual = print(f'O nivel atual de gasolina e de: {self.gasolina:.2f}')
        return nivel_atual
    
    def adicionarGasolina(self, adicionar):
        self.gasolina += adicionar