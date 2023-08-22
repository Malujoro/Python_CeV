print('Soma de todos os ímpares múltiplos de três entre 1 e 500')
soma = 0
cont = 0
for c in range(3, 501, 6):
    soma += c
    cont += 1
print(f'A s de todos os {cont} valores solicitados é {soma}')
