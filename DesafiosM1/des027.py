nome = str(input('Digite seu Nome completo: ')).strip()
no = nome.split()
prim = no[0]
ult = no[-1]
print('Prazer em te conhecer \n'
      'Primeiro nome: {0} \n'
      'Último nome: {1}'
      .format(prim, ult))
