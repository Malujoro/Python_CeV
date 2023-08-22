lin = '-' * 30
while True:
    ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    while True:  # Garantir que digite um número de 0 a 20
        n = int(input(f'{lin}\nDigite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {ext[n]}\n{lin}')
    while True:  # Garantir que digite S ou N
        cont = input(f'Quer continuar? [S/N] ').strip().upper()[0]
        if cont in 'SN':
            break
    if cont in 'N':  # Finaliza o programa se continue for N
        break
print('Fim do programa')
