from random import randint
pc = randint(0, 10)
tent = 0
acertou = False
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while not acertou:
    player = int(input('Qual é seu palpite? '))
    tent += 1
    if player == pc:
        acertou = True
    else:
        if player > pc:
            print('Menos...', end=' ')
        elif player < pc:
            print('Mais...', end=' ')
        print('Tente novamente')
print(f'Parabéns! Você acertou com {tent} tentativas')
