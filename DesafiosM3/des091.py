from random import randint
from time import sleep
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ordem = []
lista2 = {}
cont = 0
# Escreve quais foram os reultados, e adiciona os números em uma lista
print('Valores sorteados:')
for k, v in jogos.items():
    print(f'   O {k} tirou {v}')
    sleep(1)
    ordem.append(v)
# Coloca a lista em ordem
ordem.sort(reverse=True)
# Cria um outro dicionário os jogadores em ordem
while len(lista2) < 4:
    for k, v in jogos.items():
        # SE o número na posição da ordem for IGUAL ao número do DADO
        # E o jogador não estiver dentro do dicionário
        # Adiciona o jogador e o dado no dicionário
        if ordem[(len(lista2))] == v and k not in lista2:
            lista2[k] = v
        if len(lista2) == 4:
            break
# Demonstra os resultados
print('Ranking dos jogadores: ')
for k, v in lista2.items():
    cont += 1
    print(f'   {cont}º lugar: {k} com {v}')
    sleep(1)
