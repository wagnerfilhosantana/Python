def num_maior(n1,n2,n3):
    maior = n1
    if n1 < n2 and n3 < n2:
        maior = n2
    elif n1 < n3 and n2 < n3:
        maior = n3
    return maior
def num_menor(n1,n2,n3):
    menor = n1
    if n1 > n2 and n3 > n2:
        menor = n2
    elif n1 > n3 and n2 > n3:
        menor = n3
    return menor
n1 = int(input('Digite um primeiro numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terceiro numero: '))
maior = num_maior(n1,n2,n3)
menor = num_menor(n1,n2,n3)
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')