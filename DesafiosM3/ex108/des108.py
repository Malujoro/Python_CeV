from DesafiosM3.ex108 import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}'
      f'\nO dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}'
      f'\nAumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}'
      f'\nReduzindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}')
