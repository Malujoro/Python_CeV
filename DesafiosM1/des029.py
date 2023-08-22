vel = float(input('Digite a velocidade de um carro, em Km/h: '))
if vel > 80:
    multa = 7 * (vel - 80)
    print('MULTADO!! Você ultrapassou o limite de 80Km/h \n'
          'Você deve pagar a multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
