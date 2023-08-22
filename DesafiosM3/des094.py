cadastro = list()
pessoa = dict()
totidade = media = 0
lin = '-' * 60
while True:
    print(lin)
    while True:
        pessoa['nome'] = str(input('Nome: ').strip().capitalize())
        if pessoa['nome'] != '':
            break
        print('ERRO! Digite um nome válido')
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ').strip().upper())
        if pessoa['sexo'] != '' and pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    while True:
        pessoa['idade'] = str(input('Idade: ').strip())
        if pessoa['idade'] != '' and pessoa['idade'][0] in '0123456789':
            pessoa['idade'] = int(pessoa['idade'])
            totidade += pessoa['idade']
            break
        print('ERRO! Digite apenas números')

    cadastro.append(pessoa.copy())
    pessoa.clear()

    while True:
        cont = str(input('Continuar? [S/N]: ').strip().upper())
        if cont != '' and cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if cont in 'N':
        break

print(lin)

media = totidade / len(cadastro)

print(f'> Total de pessoas cadastradas: {len(cadastro)}'
      f'\n> Média de idade: {media:.2f}'
      f'\n> Lista de Mulheres: ', end='')
for p in cadastro:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}; ', end='')
print(f'\n> Lista de pessoas com idade acima da média: ')
for p in cadastro:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print(f'\n{lin}\n<< ENCERRADO >>')
