lista = []
dados = []
pesado = leve = 0
npes = nlev = ''

while True:
    cont = ' '
    # Coleta Nome e Peso
    dados.append(str(input('Nome: ').capitalize()))
    dados.append(float(input('Peso: ')))
    # Descobre o Maior e Menor peso
    if len(lista) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    # Adiciona os dados na lista principal
    lista.append(dados[:])
    dados.clear()
    # "Tratamento" da resposta de Continuar
    while True:
        cont = str(input('Continuar? [S/N] ')).strip().upper()
        if cont != '' and cont[0] in 'SN':
            break
    if cont in 'N':
        break
# Descobre quem são as pessoas com o Maior e Menor pesos
for p in lista:
    if p[1] == pesado:
        npes += f'[{p[0]}] '
    if p[1] == leve:
        nlev += f'[{p[0]}] '
# Demonstra os resultados
print('-=' * 25)
print(f'Ao todo, você cadastrou {len(lista)} pessoas\n'
      f'O maior peso foi de {pesado:.2f}Kg. Peso de {npes}\n'
      f'O menor peso foi de {leve:.2f}Kg. Peso de {nlev}')
