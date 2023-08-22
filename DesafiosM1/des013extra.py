p = float(input('Insira o Preço do Produto: R$'))
vista = p - (p * (10/100))
parcelado = p + (p * (8/100))
parcela = parcelado / 12
print('Se pagar à vista, será aplicado um desconto de 10% \n'
      'Logo, o preço será R${0:.2f} \n'
      'Se pagar parcelado, será aplicado um aumento de 8% \n'
      'As parcelas em 12x serão de R${2:.2f}, com o preço total sendo R${1:.2f}'
      .format(vista, parcelado, parcela))