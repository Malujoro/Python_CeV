n = int(input('Digite um Número entre 0 e 9999: '))
num = str(n + 10000)
uni = num[4]
dez = num[3]
cen = num[2]
mil = num[1]
print('Analisando o número {0}... \n'
      'Unidade: {1} \n'
      'Dezena:  {2} \n'
      'Centena: {3} \n'
      'Milhar:  {4} \n'
      .format(n, uni, dez, cen, mil))
