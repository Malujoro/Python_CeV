from DesafiosM3.ex109 import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}\n'
      f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}\n'
      f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}\n'
      f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}\n')
