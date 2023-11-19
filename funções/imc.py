
massa = float(input("Digite sua massa: "))
altura = float(input("Digite sua altura: "))
res = float(massa/pow(altura,2))
print(f'Seu Índice de Massa Corporal é {res:.2f}')
if res < 15.99:
    print("Você está a baixo do peso no grau III.")
elif res >= 16.00 and res <= 16.99:
    print("Você está a baixo do peso no grau II.")
elif res >= 17.00 and res <= 18.49:
    print("Você está a baixo do peso no grau I.")
elif res >= 18.50 and res <= 24.99:
    print("Você está no peso ideal.")
elif res >= 25.00 and res <= 29.99:
    print("Você está com sobrepeso.")
elif res >= 30.00 and res <= 34.99:
    print("Você está com obesidade de grau I.")
elif res >= 35.00 and res <= 39.99:
    print("Você está com obesidade de grau II.")
elif res >= 40:
    print("Você está com obesidade de grau III.")
