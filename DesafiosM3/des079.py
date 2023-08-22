lista = []
while True:
    print('-' * 40)
    cont = ' '
    n = (int(input(f'Digite um valor: ')))

    # if n not in lista:
    if lista.count(n) == 0:
        print('Valor \033[32madicionado\033[m com sucesso...')
        lista.append(n)
    else:
        print('Valor \033[35mduplicado\033[m! Não vou adicionar')

    while cont not in 'SN':
        cont = str(input(f'Quer continuar? [S/N] ').strip().upper()[0])
    if cont in 'N':
        break
print('-=' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')
