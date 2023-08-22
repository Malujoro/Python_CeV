lista = []
while True:
    cont = ' '
    lista.append(int(input('Digite um número: ')))
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
lista.sort(reverse=True)
print('-=' * 20)
print(f'''> Foram digitados {len(lista)} números
> Lista decrescente {lista}''')
if 5 in lista:
    print('> O valor 5 não foi encontrado na lista')
else:
    print('> O valor 5 faz parte da lista')
