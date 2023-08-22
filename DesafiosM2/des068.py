from random import randint
lin = '-=' * 15
lin2 = '-' * 30
tot = 0
print(f'{lin}\nVAMOS JOGAR PAR OU ÍMPAR\n{lin}')
while True:
    op = ' '
    player = int(input('Diga um valor: '))
    pc = randint(0, 10)
    while op not in 'PI':
        op = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    soma = player + pc
    if soma % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    print(f'Você jogou {player} e o computador {pc}. Total de {soma} DEU {r}\n{lin2}')
    if r[0] == op:
        print(f'Você GANHOU!\nVamos jogar novamente...\n{lin}')
        tot += 1
    else:
        print('Você PERDEU!!!')
        break
print(f'{lin}\nGAME OVER! Você venceu {tot} vezes')
