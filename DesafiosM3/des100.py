from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    lista.clear()
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        lista.append(n)
        sleep(0.3)
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa Principal
sorteia(numeros)
soma_par(numeros)
