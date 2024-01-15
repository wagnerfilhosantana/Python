
def convertercelsius(temperatura, conversao):
    if conversao == 'f' or conversao == 'F':
        celsius = (temperatura - 32) * 5/9
        
    else: 
        celsius = temperatura - 273.15

    return celsius

def converterfahrenheit(temperatura, conversao):
    if conversao == 'c' or conversao == 'C':
        fahrenheit = (temperatura + 32) * 9/5
        
    else:
        fahrenheit = (temperatura- 273.15) * 5/9 + 32

    return fahrenheit

def converterkelvin(temperatura, conversao):
    if conversao == 'c' or conversao == 'C':
        kelvin = temperatura + 273.15
    else:
        kelvin = (temperatura - 32) * 5/9 + 273.15

    return kelvin

def graus():
    escalademedida = str(input('Digite a escala de medida que voce quer converter, sendo c para Celsius f para Fahrenheit e k para Kelvin: '))

    if escalademedida not in ['c', 'f', 'k']:
        print("Escala de medida inválida. Por favor, digite 'c', 'f' ou 'k'.")
        return

    if escalademedida == 'c':
        conversao = input('Digite f para fahrenheit ou k para Kelvin: ')
        if conversao not in ['f', 'k']:
            print("Unidade de conversão inválida. Por favor, digite 'f' ou 'k'.")
            return 
        temperatura = float(input('Digite a temperatura: '))
        resultado = convertercelsius(temperatura, conversao)
    elif escalademedida == 'f':
        conversao = input('Digite c para Celsius ou k para Kelvin: ')
        if conversao not in ['c', 'k']:
            print("Unidade de conversão inválida. Por favor, digite 'c' ou 'k'.")
            return
        temperatura = float(input('Digite a temperatura: '))
        resultado = converterfahrenheit(temperatura, conversao)
    else:
        conversao = input('Digite f para fahrenheit ou c para Celsius: ')
        if conversao not in ['f', 'c']:
            print("Unidade de conversão inválida. Por favor, digite 'f' ou 'c'.")
            return
        temperatura = float(input('Digite a temperatura: '))
        resultado = converterkelvin(temperatura, conversao)
    print(f"A temperatura convertida fica: {resultado:.2f}")

while True:
    graus()
    parar = input("DEseja continuar, s ou n?")
    if parar == "s":
        continue
    else:
        break


    