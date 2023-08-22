def leia_int(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return int(n)


def leia_float(txt):
    while True:
        try:
            n = str(input(txt)).replace(',', '.')
            n = float(n)
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return float(n)


nint = leia_int('Digite um Inteiro: ')
nfloat = leia_float('Digite um Real: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {nfloat}')
