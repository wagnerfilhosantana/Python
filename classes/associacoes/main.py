from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joaozinho')
caneta = Caneta('Bic')
Maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
Maquina.escrever()