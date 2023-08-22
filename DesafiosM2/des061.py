print('Gerador de PA')
print('-=' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(n, end=' → ')
    n += r
    c += 1
print('FIM')
