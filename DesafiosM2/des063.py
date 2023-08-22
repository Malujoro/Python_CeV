n1 = 0
n2 = 1
lin = '-' * 30
c = 3
print(f'{lin}\nSequência de Fibonnaci\n{lin}')
n = int(input('Quantos termos você deseja? '))
print(f'{lin}\n{n1} → {n2}', end=' → ')
while c <= n:
    n3 = n1 + n2  # n3 soma os valores de n1 e n2 (inicialmente 0 + 1)
    n1 = n2  # n1 recebe o valor antigo de n2 (inicialmente 1)
    n2 = n3  # n2 recebe o valor antigo de n3 (inicialmente 1)
    print(n3, end=' → ')
    c += 1
print(f'FIM\n{lin}')
