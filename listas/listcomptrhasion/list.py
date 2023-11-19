#Lista normal
lista_precos = [100, 1500, 2000, 50, 250]

nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)  
print(nova_lista_precos)

nova_lista_precos2 = [preco * 0.5 for preco in lista_precos]
print(nova_lista_precos2)


imposto = []
for preco in lista_precos:
    if preco > 200:
        imposto.append(preco * 0.10)
print(imposto)

impostos = [preco * 0.20 for preco in lista_precos if preco > 200]
print(impostos)