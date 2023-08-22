lista = [[], [], []]
# lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha].append(int(input(f'Digite o valor para [{linha}, {coluna}]: ')))
        # lista[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))

print('-=' * 20)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end=' ')
    print()
