print('-' * 20,
      '\nEMPRÉSTIMO BANCÁRIO\n' +
      '-' * 20)
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
parc = anos * 12
pmen = float(casa / parc)
print('-' * 20)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'
      .format(casa, anos, pmen))
if pmen <= (sal * 0.3):
    print('O empréstimo será REALIZADO, com {} parcelas'.format(parc))
else:
    print('Infelizmente o empréstimo foi NEGADO. \nA parcela excede 30% do seu salário')
