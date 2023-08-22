lista = []
par = []
impar = []
while True:
    cont = ' '
    lista.append(int(input('Digite um número: ')))
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N] ')).strip().upper()
        if cont != '':
            cont = cont[0]
    if cont in 'N':
        break

for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('-=' * 30)
print(f'''> A lista completa é {lista}
> A lista de pares é {par}
> A lista de ímpares é {impar}''')
