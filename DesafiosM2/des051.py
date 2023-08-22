print('=' * 40)
print('10 TERMOS DE UMA PA'.center(40))
print('=' * 40)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
    print(f'{n}', end=' → ')
    n += r
print('acabou')
