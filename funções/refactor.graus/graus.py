f = 0
c = 0
k = 0
graus = ""
formula = str(input("Digite a formula que voce queira converter, sendo 'c' para graus Celsius, 'f' para Fahrenheit ou 'k' para Kelvin: "))

def Fahrenheit(f, c, k):
    if formula in {'f', 'F'}:
         graus = str(input("Qual Graus voce quer converter em Kelvin 'k' ou em Celsius 'c': "))
         if graus in {'c', 'C'}:     
            c = float(input("Digte o Graus em Celsius para converter: "))
            f = (c * 5/9) + 32
         elif graus in {'k', 'K'}:
            k = float(input("Digite a temperatura em Kelvin para converter: "))
            f = (k - 273.15) * 5/9 + 32
    return f

def Celsius(f, c, k):
    if formula == "c" or formula == "C":
        graus = input("Qual Grau voce quer converter em Kelvin 'k' ou em Fahrenheit 'f': ")
        if graus == 'f' or graus == 'F':     
            f = float(input("Digite a temperatura em Fahrenheit para converter: "))  
            c = (f - 32) * 5/9
        elif graus == 'k' or graus == 'K':
            k = float(input("Digite a temperatura em Kelvin para converter: "))
            c = k - 273.15
    return c
def Kelvin(f, c, k):
    if formula == 'k' or formula == 'K':
        graus = input("Qual Grau voce quer converter em Celsius 'c' ou em Fahrenheit 'f':")   
        if graus == 'c' or graus == 'C':
            c = float(input("Digite a temperatura em Celsius para converter: "))     
            k = c + 273.15
        elif graus == 'f' or graus == 'F':
            f = float(input("Digite a temperatura em Fahrenheit para converter: "))
            k = (f - 32) * 5/9 + 273.15
    return k        
graus1 = Fahrenheit(f, c, k)
graus2 = Celsius(f, c, k)
graus3 = Kelvin(f, c, k)
if formula == 'f' or formula == 'F':
    print(f"A temperatura em Fahrenheit e: {graus1:.2f}")
elif formula == 'c' or formula == 'C':
    print(f"A temperatura em Celsius e: {graus2:.2f}")
elif formula == 'k' or formula == 'K':
    print(f"A temperatura em Kelvin e: {graus3:.2f}")
else:
    print("Nenhum parametro encontrado")