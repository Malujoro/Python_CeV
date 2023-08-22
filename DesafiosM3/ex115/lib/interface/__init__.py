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


def linha(tam=50):
    return '-' * tam


def cor(txt, tinta='base'):
    cores = {'base': '\033[m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m',
             'roxo': '\033[35m',
             'ciano': '\033[36m'}
    return f'{cores[tinta]}{txt}{cores["base"]}'


def cabecalho(txt='MENU'):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor(c, "amarelo")} - {cor(item, "azul")}')
        c += 1
    print(linha())
    opc = leia_int(f'{cor("Sua Opção: ", "amarelo")}')
    return opc

