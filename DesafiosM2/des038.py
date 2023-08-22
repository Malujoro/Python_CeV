n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor {} é o MAIOR'.format(n1))
elif n2 > n1:
    print('O SEGUNDO valor {} é o MAIOR'.format(n2))
else:
    print('Não existe valor maior, os dois são IGUAIS')
