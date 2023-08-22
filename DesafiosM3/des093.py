jogador = {'nome': str(input('Nome do jogador: ').capitalize())}
partidas = list()
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
lin = '-=' * 30
# Recebe os gols de cada partida
for c in range(0, jogos):
    partidas.append(int(input(f'    Quantos gols na {c+1}ª partida? ')))
# Guarda os gols por partida e o total de gols
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
# Mostra o dicionário
print(f'{lin}\n{jogador}\n{lin}')
# Mostra os valores de cada campo
for k, v in jogador.items():
    print(f'O campo {k.capitalize()} tem o valor {v}.')
# Mostra a última "tabela", com a quantidade de gols por partida
print(f'{lin}\nO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, g in enumerate(partidas):
    print(f'    > Na {p + 1}ª partida, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
# Mostra o rendimento do jogador
print(f'{lin}\n{jogador["nome"]} teve um rendimento de {jogador["total"]} gols em {jogos} partidas')
