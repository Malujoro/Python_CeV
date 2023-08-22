n = int(input('Insira um número: '))
soma = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'[{c}]', end=' ')
        soma += 1
    else:
        print(c, end=' ')
print(f'\nO número {n} foi divisível {soma} vezes ')
if soma == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO')
