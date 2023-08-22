lin = '-=' * 20

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

print(f'{lin}\n> Você digitou os valores {n}')
print(f'> O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'> O número 3 apareceu na {n.index(3)+1}º posição')
else:
    print('> O valor 3 não foi digitado em nenhuma posição')
print(f'> Os valores pares digitados foram:', end=' ')
for i in n:
    if i % 2 == 0:  # Confere quantos pares
        print(i, end=' ')
