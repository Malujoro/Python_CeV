lista = []
maior = menor = 0
pmai = pmen = ''

for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da {c}º posição: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('-=' * 30)

for p, n in enumerate(lista):
    if n == maior:
        pmai += f'{p}... '
    if n == menor:
        pmen += f'{p}... '

print(f'''Você digitou os valores {lista}
O \033[:32mmaior\033[m valor digitado foi {maior} nas posições {pmai}
O \033[:31mmenor\033[m valor digitado foi {menor} nas posições {pmen}''')
