def escreva(txt):
    """
    -> Função para criar títulos com linhas de tamanhos diferentes
    :param txt: Título
    ~Função criada por Mateus
    """
    tam = len(txt) + 4
    print('~' * tam)
    print(txt.center(tam))
    print('~' * tam)


# Programa Principal
# escreva('Olá, Mundo!')
# escreva('Gustavo Guanabara')
# escreva('Curso de Python no Youtube')
# escreva('CeV')
# escreva('シ.ン!凸')
