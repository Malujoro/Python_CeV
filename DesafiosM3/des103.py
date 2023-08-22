def ficha(nome='<desconhecidos', gols='0'):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: ').strip().capitalize())
g = str(input('Número de Gols: ').strip())
ficha(n, g)
