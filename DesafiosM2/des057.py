sexo = input('Digite seu Sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
