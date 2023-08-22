from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20,
      '\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n' +
      '-=-' * 20)
num = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if num == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {0} e não no {1}!'
          .format(computador, num))
