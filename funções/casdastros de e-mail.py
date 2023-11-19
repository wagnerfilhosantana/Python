def dominio(email):
    _inicio = email.index('@')+1
    return email[_inicio:len(email)]

email = input('Digite seu e-mail: ')
dom = dominio(email)
print(f'O seu dominio de e-mail: {dom}')
