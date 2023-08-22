matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = soma3c = maior2l = 0

for l in range(0, 3):
    for c in range(0, 3):
        # Insere os valores na Linha e Posição
        while True:
            n = input(f'Digite o valor para [{l}, {c}]: ')
            if n != '' and n[0] in '0123456789':
                matriz[l][c] = int(n)
                break
print('-=' * 15)
# Demonstra a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        # Soma os pares
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        # Soma a terceira coluna
        if c == 2:
            soma3c += matriz[l][2]
        # Procura o maior da segunda linha
        if l == 1:
            if c == 0 or matriz[1][c] > maior2l:
                maior2l = matriz[1][c]
    print()
# Demonstra os resultados
print(f'-=' * 15 +
      f'\n> Soma dos pares: {somaPar}'
      f'\n> Soma da terceira coluna: {soma3c}'
      f'\n> Maior valor da segunda linha: {maior2l}')
