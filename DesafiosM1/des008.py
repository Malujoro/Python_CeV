m = float(input('Insira uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor em Quilômetros é {0}km \n'
      'O valor em Hectômetros é {1}hm \n'
      'O valor em Decâmetros é {2}dam \n'
      'O valor em Metros é {3}m \n'
      'O valor em Decímetros é {4}dm \n'
      'O valor em Centímetros é {5}cm \n'
      'O valor em Milímetros é {6}mm'
      .format(km, hm, dam, m, dm, cm, mm))
