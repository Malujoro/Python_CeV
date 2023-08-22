nome = str(input('Digite seu nome completo: ')).strip()
maiusc = nome.upper()
minusc = nome.lower()
tot = len(nome.replace(' ', ''))
listnom = nome.split()
prim = listnom[0]
nprim = len(prim)
print('Seu nome em Maiúsculas é {0} \n'
      'Seu nome em Minúsculas é {1} \n'
      'Seu nome tem ao todo {2} letras \n'
      'Seu primeiro nome é {4} e ele tem {3} letras'
      .format(maiusc, minusc, tot, nprim, prim))
