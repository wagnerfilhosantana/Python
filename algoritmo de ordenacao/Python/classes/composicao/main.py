from classe import Cliente

cl1 = Cliente('Wagner', 19)
print('---      ---      ---')
print(cl1.nome, cl1.idade)
cl1.inserir_endereco('Lodrina,', 'Parana')
cl1.lista()
cl2 = Cliente('Wesley', 17)
print('---     ---     ---')
print(cl2.nome, cl2.idade)
cl2.inserir_endereco('Caninde,', 'Ceara')
cl2.lista()
cl3 = Cliente('Ana Kelly', 14)
print('---     ---     ---')
print(cl3.nome, cl3.idade)
cl3.inserir_endereco('Palmas,', 'Tocantins')
cl3.lista()
cl4 = Cliente('Cleonice', 1000)
print('---     ---     ---')
print(cl4.nome, cl4.idade)
cl4.inserir_endereco('Ouro Preto,', 'Sao Paulo')
cl4.lista()
print('---      ---      ---')