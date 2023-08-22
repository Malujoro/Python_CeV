nome = str(input('Digite o nome de uma cidade: ')).strip()
santo = 'SANTO' in nome[:5].upper()
print('A cidade digitada começa com o nome Santo? {0}'
      .format(santo))
