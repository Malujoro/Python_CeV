from math import radians, sin, cos, tan
n = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))
print('O ângulo de {0} tem o SENO de {1:.2f} \n'
      'O ângulo de {0} tem o COSSENO de {2:.2f} \n'
      'O ângulo de {0} tem a TANGENTE de {3:.2f}'
      .format(n, sen, cos, tan))
