lin = '-' * 25
tot18 = toth = m20 = 0
while True:
    cont = sexo = 'a'
    print(f'{lin}\n', 'CADASTRE UMA PESSOA'.center(23), f'\n{lin}')
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print(lin)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont in 'N':
        break
print(' FIM DO PROGRAMA '.center(30, '='))
print(f'''Total de pessoas com mais de 18 anos: {tot18}
Ao todo temos {toth} homens cadastrados
E temos {m20} mulheres com menos de 20 anos''')
