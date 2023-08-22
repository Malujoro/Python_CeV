sal = float(input('Digite seu salário: R$'))
if sal > 1250:
    nsal = sal + (sal * (10/100))
else:
    nsal = sal + (sal * (15/100))
print('Antes ganhava R${0:.2f}, e agora ganhará R${1:.2f}'.format(sal, nsal))
