from DesafiosM3.ex107 import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}\n'
      f'O dobro de R${preco} é R${moeda.dobro(preco)}\n'
      f'Aumentando 10%, temos R${moeda.aumentar(preco, 10)}\n'
      f'Reduzindo 13%, temos R${moeda.diminuir(preco, 13)}\n')
