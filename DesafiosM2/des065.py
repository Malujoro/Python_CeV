cont = 'soma'
tot = media = soma = maior = menor = 0
while cont == 'soma':
    tot += 1
    n = int(input('Digite um Número: '))
    soma += n
    cont = input('Continuar? [S/N]: ').strip().lower()[0]
    if tot == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / tot
print('-' * 30)
print(f'''> {tot} números foram digitados
> Média de {media:.2f}
> Maior número: {maior}
> Menor número: {menor}''')
