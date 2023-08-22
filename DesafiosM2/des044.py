print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] - à vista dinheiro/cheque
[2] - à vista cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão''')
forma = int(input('Opção: '))
if forma == 1:
    final = preco * 0.9
    print('Aplicando 10% de desconto')
elif forma == 2:
    final = preco * 0.95
    print('Aplicando 5% de desconto')
elif forma == 3:
    final = preco
    parc = final / 2
    print('Sem descontos ou Juros\n'
          'Compra de 2 parcelas de R${:.2f}. '.format(parc), end='')
elif forma == 4:
    final = preco * 1.2
    n = int(input('Quantas parcelas? '))
    parc = final / n
    print('Aplicando 20% de Juros\n'
          'Compra de {} parcelas de R${:.2f}. '.format(n, parc), end='')
else:
    final = preco
    print('ERRO! forma de pagamento não reconhecida')
print('O preço final será R${:.2f}'.format(final))
