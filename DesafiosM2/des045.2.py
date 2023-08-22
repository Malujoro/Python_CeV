from random import randrange
pe = 'PEDRA'
pa = 'PAPEL'
te = 'TESOURA'
lin = '-' * 23
cont = 's'
while cont == 's' or cont == 'S':
    print(lin)
    print(pe, pa, te)
    print(lin)
    print('Suas opções:'
          '\n[1]', pe,
          '\n[2]', pa,
          '\n[3]', te)
    play = input('Escolha sua jogada: ')
    comp = randrange(1, 4)
    pedra = 'O computador escolheu ' + pe
    papel = 'O computador escolheu ' + pa
    tesoura = 'O computador escolheu ' + te
    result = 0
    print(lin)
    if play == '1':
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
    elif play == '2':
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
    elif play == '3':
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
    else:
        print('ERRO!! jogada não reconhecida')
    if result == 'GANHOU':
        print('Parabéns, você GANHOU!')
    elif result == 'EMPATE':
        print('EMPATE!!')
    elif result == 'PERDEU':
        print('Que pena, você PERDEU!')
    print(lin)
    cont = str(input('Continuar? [s/n]: '))
