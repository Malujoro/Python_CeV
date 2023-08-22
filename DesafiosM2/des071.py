lin = '=' * 30
print(f'{lin}\n', 'BANCO MRS'.center(28), f'\n{lin}')
total = n = int(input('Que valor você quer sacar? R$'))
n50 = n20 = n10 = n1 = 0
while True:
    if n >= 50:
        n50 = n // 50
        n -= n50 * 50
        print(f'Total de {n50} cédulas de R$50')
    elif n >= 20:
        n20 = n // 20
        n -= n20 * 20
        print(f'Total de {n20} cédulas de R$20')
    elif n >= 10:
        n10 = n // 10
        n -= n10 * 10
        print(f'Total de {n10} cédulas de R$10')
    elif n >= 1:
        n1 = n
        n -= n1
        print(f'Total de {n1} cédulas de R$1')
    elif n == 0:
        break
print(f'{lin}\nVolte sempre ao BANCO MRS! Tenha um bom dia')
