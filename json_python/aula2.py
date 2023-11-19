import json

jogador = '{"nome" : "Wagner","time" : "aviador", "Vivo" : "True", "Energia" : 100, "Mochila" : ["penerdeira", "corda","linha", "arame"], "Aeronaves" : [{"tipo" : "transporte", "habilidade" : 80},{"tipo" : "ataque", "habilidade" : 100},{"tipo" : "reconhecimento", "habilidade" : 50}]}'

jogador_json = json.loads(jogador)

print(jogador_json["Aeronaves"])

element = jogador[str("Aeronaves")]

print(element["tipo"])

for a in jogador_json["Aeronaves"]:
    print(a)