s = float(input('Insira o Salário: R$'))
sf = s + (s * (15/100))
print('O salário era de R${0:.2f} \n'
      'Após o aumento de 15%, o salário ficou R${1:.2f}'
      .format(s, sf))
