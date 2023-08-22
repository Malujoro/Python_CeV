# from math import factorial
# n = int(input('Fatorial de: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

n = cont = int(input('Fatorial de: '))
r = 1
print(f'Calculando {n}! = ', end='')
while cont > 0:
    r *= cont
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(f'{r}')

# n = int(input('Fatorial de: '))
# r = 1
# print(f'Calculando {n}! = ', end='')
# for c in range(n, 0, -1):
#     r *= c
#     print(f'{c}', end='')
#     print(f' x ' if c > 1 else ' = ', end='')
# print(f'{r}')
