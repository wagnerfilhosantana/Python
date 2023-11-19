import random

while True:
    num_computer = random.randrange(0,9)
    num_usuario = int(input('Adivinhe o numero que estou pensando: '))

    if num_usuario == num_computer:
        print('Muito bem! Voce acertou!')
        break
    else:
        print(f'Que pena! Voce errou, o numero era {num_computer}.')
