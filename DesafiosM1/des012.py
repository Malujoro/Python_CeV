p = float(input('Insira o preço do produto, em R$'))
pf = p - (p * (5/100))
print('O produto custava R${0:.2f} \n'
      'Após o desconto de 5%, o produto vai custar R${1:.2f}'
      .format(p, pf))
