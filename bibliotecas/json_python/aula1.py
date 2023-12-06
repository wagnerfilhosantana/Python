import json

carros_json = '{"Marca":"Honda", "Modelo":"HRV", "Cor":"prata"}'

carros = {"Marca":"Ferrari", "Modelo":"328", "Cor":"vermelha"}

carro = json.loads(carros_json)

print(carros)
print('-'*50)
for c in carro:
    print(c)

print('-'*10)

for v in carro.values():
    print(v)

print('-'*15)

for i in carro.items():
    print(i)

print('-'*15)

for k,v in carro.items():
    print(k,v)