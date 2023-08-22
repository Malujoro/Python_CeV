frase = str(input('Digite uma frase: ')).strip().upper()
quant = frase.count('A')
onde1 = frase.find('A') + 1
onde2 = frase.rfind('A') + 1
print('Quantas vezes aparece a letra A? {0} \n'
      'Em que posição ela aparece pela primeira vez? {1} \n'
      'Em que posição ela aparece pela última vez? {2} \n'
      .format(quant, onde1, onde2))
