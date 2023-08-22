def leia_dinheiro(txt='Digite o preço: R$'):
    """
    -> Função para que o usuário digite um preço
    :param txt: O texto a ser exibido
    :return: O valor digitado
    """
    while True:
        preco = str(input(txt)).strip().replace(',', '.')
        if preco.isnumeric() or len(preco) > 3 and preco.count('.') == 1:
            return float(preco)
        else:
            print(f'\033[31mERRO! \"{preco}\" é um preço inválido!\033[m')
