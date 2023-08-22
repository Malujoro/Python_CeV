lin = '=' * 30
print(f'{lin}\n', 'BANCO MRS'.center(28), f'\n{lin}')
total = n = int(input('Que valor você quer sacar? R$'))
ced = 50
totced = 0
while True:
    if total >= ced:
        totced = total // ced
        total -= totced * ced
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(f'{lin}\nVolte sempre ao BANCO MRS! Tenha um bom dia')
