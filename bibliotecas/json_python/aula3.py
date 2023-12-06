import json

with open('C:/Users/wagne/OneDrive/Documentos/GitHub/Python/json_python/file.json') as file:
    jogador_json = json.load(file)


"""print(jogador_json["Aeronaves"])

print('-'*50)

print(jogador_json['Aeronaves'][2]['tipo'])

print('-'*50)

for a in jogador_json["Aeronaves"]:
    print(a)
    print('-'*50)"""

for c in jogador_json.items():
    print(c)

for im in jogador_json['Mochila']:
    print(f'| {im} |')
    print('-'*9)