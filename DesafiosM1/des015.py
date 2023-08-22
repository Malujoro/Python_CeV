dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
#diastot = dias * 60
#kmtot = km * 0.15
#total = diastot + kmtot
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${0:.2f}'.format(total))