from random import randint
from time import sleep
# Nomeia as variáveis responsáveis pelo nome e cor das opções
pe = '\033[0;32mPEDRA\033[0;30;m'
pa = '\033[0;33mPAPEL\033[0;30;m'
te = '\033[0;36mTESOURA\033[0;30;m'
lin = '-' * 23
cont = 's'
while cont == 's' or cont == 'S':
    # Menu do jogo
    print(lin)
    print(pe, pa, te)
    print(lin)
    print('Suas opções:'
          '\n[1]', pe,
          '\n[2]', pa,
          '\n[3]', te)
    # Player e Computador fazem suas jogadas
    play = input('Escolha sua jogada: ')
    comp = randint(1, 3)
    pedra = 'O computador escolheu ' + pe
    papel = 'O computador escolheu ' + pa
    tesoura = 'O computador escolheu ' + te
    result = 0
    print(lin)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print(lin)
    if play == '1': # Se o jogador escolher PEDRA
        print('Você escolheu ' + pe)
        if comp == 1:
            print(pedra)
            result = 'EMPATE'
        elif comp == 2:
            print(papel)
            result = 'PERDEU'
        elif comp == 3:
            print(tesoura)
            result = 'GANHOU'
    elif play == '2': # Se o jogador escolher PAPEL
        print('Você escolheu ' + pa)
        if comp == 1:
            print(pedra)
            result = 'GANHOU'
        elif comp == 2:
            print(papel)
            result = 'EMPATE'
        elif comp == 3:
            print(tesoura)
            result = 'PERDEU'
    elif play == '3': # Se o jogador escolher TESOURA
        print('Você escolheu ' + te)
        if comp == 1:
            print(pedra)
            result = 'PERDEU'
        elif comp == 2:
            print(papel)
            result = 'GANHOU'
        elif comp == 3:
            print(tesoura)
            result = 'EMPATE'
    # Se o jogador escolher OUTRO
    else:
        print('ERRO!! jogada não reconhecida')
    # Resultados do Jogo
    if result == 'GANHOU':
        print('Parabéns, você {}GANHOU{}!'.format('\033[0;32;4m', '\033[0;30;m'))
    elif result == 'EMPATE':
        print('{}EMPATE!!{}'.format('\033[0;34;4m', '\033[0;30;m'))
    elif result == 'PERDEU':
        print('Que pena, você {}PERDEU!{}'.format('\033[0;31;4m', '\033[0;30;m'))
    print(lin)
    cont = str(input('Continuar? [s/n]: '))
