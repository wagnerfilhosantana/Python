def soma(n1,n2,n3):
    s = n1+n2+n3
    return s
def media(n1,n2,n3):
    m = soma(n1,n2,n3)/3
    return m
n1 = int(input('Digite um primeir numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terciro e ultimo numero: '))
soma_arg = soma(n1,n2,n3)
media_arg = media(n1,n2,n3)
print(f'A soma dos numeros mencionado e {soma_arg} e a sua media e {media_arg}')