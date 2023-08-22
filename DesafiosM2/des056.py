idtot = 0  # Idade total
midtot = 0  # Média idade total
idhvelho = 0  # Idade do homem mais velho
nhvelho = ''  # Nome do homem mais velho
totmvinte = 0  # Quantidade de mulheres com menos de 20 anos
for c in range(1, 5):
    # Layout de perguntas
    print(f'{c}º PESSOA'.center(19, '-'))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idtot += idade  # Soma da Média
    # Atribui a idade e nome do PRIMEIRO homem, como sendo o mais velho
    if c == 1 and sexo == 'M':
        idhvelho = idade
        nhvelho = nome
    # Nome do Homem mais velho
    if sexo == 'M' and idade > idhvelho:
        idhvelho = idade
        nhvelho = nome
    # Quantidade de Mulheres jovens
    if sexo == 'F' and idade < 20:
        totmvinte += 1
midtot = idtot / 4  # Divisão da média
# Resultados
print(f'''A média de idade do grupo é {midtot} anos
O homem mais velho tem {idhvelho} e se chama {nhvelho}
Ao todo são {totmvinte} mulheres com menos de 20 anos''')
