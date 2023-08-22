def leia_int(txt):
    print('-' * 30)
    while True:
        num = str(input(txt).strip())
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
