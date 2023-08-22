n1 = int(input('Insira um Número: '))
n2 = int(input('Insira mais um Número: '))
s = n1 + n2
print('A soma entre {4}{0}{3} e {5}{1}{3} é igual a {6}{2}{3}'
      .format(n1, n2, s, '\033[m', '\033[31m', '\033[32m', '\033[36m'))
