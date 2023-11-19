import re

texto_qualquer = 'Isto e um teste sobre o teste de expressoes regulares em teste.'
print('\n')
print(re.findall(r'teste',texto_qualquer))
print(re.search(r'teste', texto_qualquer))
print(re.sub(r'teste', 'eu sou cara',  texto_qualquer))

print('\n')

those_text = re.compile(r'teste')
print(those_text.findall(texto_qualquer))
print(those_text.search(texto_qualquer))
print(those_text.sub('consegui', texto_qualquer))

print('\n')