# from math import pow, sqrt
# co = float(input('Comprimento do Cateto Oposto: '))
# ca = float(input('Comprimento do Cateto Adjacente: '))
# hip = sqrt(pow(co, 2) + pow(ca, 2))
# print('A Hipotenusa vai medir {0:.2f}'.format(hip))

from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir {0:.2f}'.format(hip))