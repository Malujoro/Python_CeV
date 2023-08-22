from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    op = int(input('>>>>> Qual é sua opção?: '))
    if op == 1:
        r = n1 + n2
        print(f'A soma {n1} + {n2} = {r}')
    elif op == 2:
        r = n1 * n2
        print(f'O resultado de {n1} x {n2} = {r}')
    elif op == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
        print(f'Entre {n1} e {n2} o maior valor é {r}')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('-' * 31)
    sleep(2)
print('Programa finalizado')
