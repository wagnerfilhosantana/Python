a = int(input("Digite um numero da base:"))
b = int(input("Digite um numero da potencia: "))
def potencia(a,b):
    resposta = 1
    i = 0
    while i < b:
        resposta = a * resposta
        i = i + 1
    return resposta
res = potencia(a, b)
print(res)