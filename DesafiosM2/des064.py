c = tot = soma = 0
while c != 999:
    c = int(input('Digite um número [999 para parar]: '))
    if c != 999:
        tot += 1
        soma += c
print(f'FIM, com {tot} números digitados e uma soma de {soma}')
