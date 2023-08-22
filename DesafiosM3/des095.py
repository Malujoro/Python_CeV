cadastro = list()
jogador = dict()
gols = list()
lin = {'-': '-' * 35, '-=': '-=' * 30, '--': '-' * 45}
while True:
    print(lin['-'])
    while True:  # Cadastrar Nome
        jogador['nome'] = str(input('Nome do Jogador: ').strip().capitalize())
        if jogador['nome'] != '':
            break
    while True:  # Cadastrar o número de partidas
        partidas = str(input(f'Quantas partidas {jogador["nome"]} jogou? ').strip())
        if partidas != '' and partidas[0] in '0123456789':
            partidas = int(partidas)
            break
    for p in range(0, partidas):  # Cadastra os gols por partida
        while True:
            gol = str(input(f'   Quantos gols na {p+1}ª partida? ').strip())
            if gol != '' and gol[0] in '0123456789':
                gol = int(gol)
                gols.append(gol)
                break
    # Adiciona os Gols e o Total dentro da ficha do jogador e o Cadastra
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    cadastro.append(jogador.copy())
    gols.clear()
    while True:  # Cadastra o Continue
        cont = str(input('Continuar? [S/N]: ').strip().upper())
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if cont in 'N':
        break
print(lin['-='])  # Mostra a tabela com as informações de TODOS os jogadores
#print(f'{"cod":>3} {"nome":<13} {"gols":<18} {"total":<5}')
print(f'{"cod":>3}', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print(f"\n{lin['--']}")
for c, j in enumerate(cadastro):
    #print(f'{c:>3} {j["nome"]:<13} {str(j["gols"]):<18} {j["total"]:<5}')
    print(f'{c:>3}', end=' ')
    for k in j.values():
        print(f'{str(k):<15}', end=' ')
    print()
while True:  # Escolher jogador específico
    print(f'{lin["--"]}\nMostrar dados de qual jogador? (Enter fecha)')
    cod = str(input('cod: ')).strip()
    if cod == '':
        break
    elif cod[0] in '0123456789':
        cod = int(cod)
        if cod < len(cadastro):
            print(f' LEVANTAMENTO DO JOGADOR \033[34m{cadastro[cod]["nome"].upper()}\033[m: '.center(51, '-'))
            for c, g in enumerate(cadastro[cod]['gols']):
                print(f'   No {c+1}º jogo fez {g} gols.')
        else:
            print(f'ERRO! Não existe jogador com código {cod}. Tente novamente')
print('<< VOLTE SEMPRE >>')
