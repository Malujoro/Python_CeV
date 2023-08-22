print('Gerador de PA Infinito')
print('-=' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 10
s = 0
while c > 0:
    print(n, end=' → ')
    n += r
    c -= 1
    s += 1
    if c == 0:
        c = int(input('PAUSA\nGostaria de ver mais quantos termos?: '))
print(f'Progressão finalizada com {s} termos mostrados.')
