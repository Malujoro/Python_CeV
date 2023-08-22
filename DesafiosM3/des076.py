lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.30, 'Livro', 34.90)
lin = '-' * 40
print(f'{lin}\n', 'LISTAGEM DE PREÇOS'.center(38), f'\n{lin}')
for item in range(0, 18, 2):
    print(f'{lista[item]:.<30}R${lista[item + 1]:>7.2f}')
# for item in range(0, len(lista)):
#     if item % 2 == 0:
#         print(f'{lista[item]:.<30}', end='')
#     else:
#         print(f'R${lista[item]:>7.2f}')
print(lin)
