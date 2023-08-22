from time import sleep
cores = {'base': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m'}


def ajuda(comando):
    escreva(f'Acessando o manual do comando "{funcao}"', 'roxo')
    print(cores['vermelho'], end='')
    help(comando)
    print(cores['base'], end='')
    sleep(2)


def escreva(txt, cor='base'):
    """
    -> Escreve um título com linhas adaptáveis ao seu tamanho
    :param txt: O Título a ser escrevido
    :param cor: Cor do texto
    ~ Função criada por Mateus
    """
    tam = len(txt) + 4
    print(cores[cor], end='')
    print(f'~' * tam)
    print(f'{txt.center(tam)}')
    print('~' * tam)
    print(cores["base"], end='')
    sleep(1)


# Programa Principal
while True:
    escreva("SISTEMA DE AJUDA PyHELP", 'verde')
    funcao = input(f'{cores["azul"]} Função ou Biblioteca > {cores["base"]}').strip()
    if funcao.upper() == 'FIM':
        break
    else:
        ajuda(funcao)
escreva('ATÉ LOGO', 'ciano')
