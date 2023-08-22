from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Qual seu sexo?\n'
      '[1] Homem\n'
      '[2] Mulher')
sexo = int(input('Digite sua opção: '))
print('Quem nasceu em {} tem {} anos em {}'
      .format(nasc, idade, atual))
if sexo == 1:
    if idade < 18:
        dif = 18 - idade
        print('Você irá se alistar daqui a {} anos, em {}'
              .format(dif, dif + atual))
    elif idade == 18:
        print('Está na hora de se alistar!!')
    else:
        dif = idade - 18
        print('Já passou do tempo de se alistar, está atrasado em {} anos \n'
              'Devia ter se alistado em {}'.format(dif, atual - dif))
else:
    print('Você NÃO precisa se alistar.')