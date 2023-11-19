carro = [['modelo', 'Porche'],
         ['Fabricante', 'Nao conheco'],
         ['velocidade', 340]]

carro[2][1] = 250
carro.append(['cor', ' cinza'])
for l,c in carro:
    print(f'{l} | {c}')