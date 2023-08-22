lin = '-' * 30
print(f'{lin}\n', 'Leitor de Produtos'.center(28), f'\n{lin}')
tot = mil = menor = 0
barato = ''
while True:
    cont = ' '
    nome = input('Nome do produto: ').strip().lower().capitalize()
    p = float(input('Preço do produto: R$'))
    tot += p
    if p > 1000:
        mil += 1
    if menor == 0 or p < menor:
        barato = nome
        menor = p
    print(lin)
    while cont not in 'SN':
        cont = input('Continuar? [S/N] ').strip().upper()[0]
    print(lin)
    if cont in 'N':
        break
print(f' FIM DO PROGRAMA '.center(40, '-'))
print(f'''> Total da compra: R${tot:.2f}
> {mil} Produtos custam mais de R$1000.00
> {barato} foi o produto mais barato, custando R${menor:.2f}''')
