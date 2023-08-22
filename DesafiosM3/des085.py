lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    # Lista 0 - Pares
    # Lista 1 - Ímpares
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'-=' * 30)
print(f'> Números Pares: {lista[0]}'
      f'\n> Números Ímpares: {lista[1]}')
