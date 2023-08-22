dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dist))
if dist <= 200:
    p = dist * 0.50
else:
    p = dist * 0.45
print('O preço a ser pago será de R${:.2f}'.format(p))
