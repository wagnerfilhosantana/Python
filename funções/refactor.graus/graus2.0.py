

def convertercelsius(temperatura, conversao):
    if conversao == 'f' or conversao == 'F':
        celsius = (temperatura - 32) * 5/9
        
    else: 
        celsius = temperatura - 273.15

    return print(f'Convertido fica: {celsius:.2f} °C')

def converterfahrenheit(temperatura, conversao):
    if conversao == 'c' or conversao == 'C':
        fahrenheit = (temperatura + 32) * 9/5
        
    else:
        fahrenheit = (temperatura- 273.15) * 5/9 + 32

    return print(f'Convertido fica: {fahrenheit:.2f} °F')

def converterkelvin(temperatura, conversao):
    if conversao == 'c' or conversao == 'C':
        kelvin = temperatura + 273.15
    else:
        kelvin = (temperatura - 32) * 5/9 + 273.15

    return print(f'Convertido fica: {kelvin:.2f} °K')

def graus():
    escalademedida = str(input('Digite a escala de medida que voce quer converter, sendo c para Celsius f para Fahrenheit e k para Kelvin: '))

    if escalademedida == 'c':
        conversao = input('Digite f para fahrenheit ou k para Kelvin: ')
        temperatura = float(input('Digite a temperatura: '))
        convertercelsius(temperatura, conversao)
    elif escalademedida == 'f':
        conversao = input('Digite c para Celsius ou k para Kelvin: ')
        temperatura = float(input('Digite a temperatura: '))
        converterfahrenheit(temperatura, conversao)
    else:
        conversao = input('Digite f para fahrenheit ou c para Celsius: ')
        temperatura = float(input('Digite a temperatura: '))
        converterkelvin(temperatura, conversao)
       
while True:
    graus()


    