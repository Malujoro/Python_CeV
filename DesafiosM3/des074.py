from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# menor = min(n)
# maior = max(n)
menor = sorted(n)[0]
maior = sorted(n)[-1]
media = (n[0] + n[1] + n[2] + n[3] + n[4]) / 5
print('Os valores sorteados foram: ', end='')
for c in n:
    print(c, end=' ')
print(f'''\n> O menor valor sorteado foi {menor}
> O maior valor sorteado foi {maior}
> A média foi {media:.1f}''')
