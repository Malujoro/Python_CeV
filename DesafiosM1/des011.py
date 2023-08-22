larg = float(input('Largura da Parede, em metros: '))
alt = float(input('Altura da Parede, em metros: '))
a = larg * alt
t = a / 2
print('Sua parede tem dimensão de {0}x{1} \n'
      'Sua Área é de {2}m² \n'
      'Para pintar essa parede, você precisará de {3}l de tinta'
      .format(larg, alt, a, t))
