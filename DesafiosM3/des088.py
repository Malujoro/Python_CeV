from random import randint
from time import sleep
lista = []
dados = []
lin = '-' * 36

# Tela de início
print(f'{lin}\n', 'JOGA NA MEGA SENA'.center(34), f'\n{lin}')
jogos = int(input('Quantos jogos você quer? '))

while True:  # Cada jogo tem 6 números
    numeros = 6
    while numeros > 0:
        # Gera números. Entra no jogo se não for repetido
        n = randint(0, 60)
        if n not in dados:
            dados.append(n)
            numeros -= 1
    # Organiza em ordem numérica e adiciona na lista principal
    dados.sort()
    lista.append(dados[:])
    dados.clear()
    # Quando os jogos forem iguais a quantidade desejada, sai do looping
    if len(lista) == jogos:
        break

print(f' SORTEANDO {jogos} JOGOS '.center(36, '='))

for c in range(0, len(lista)):
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(1)
print(' < BOA SORTE! > '.center(36, '='))
