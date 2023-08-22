def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(num=0, porcentagem=0, formato=False):
    """
   -> Função para calcular um Aumento de Porcentagem
    :param num: Preço ou Número
    :param porcentagem: Quantidade do Aumento
    :param formato: {Opcional} True = Valor retorna formatado como uma moeda
    :return: O Preço após o aumento
    """
    result = num + (num * (porcentagem / 100))
    if formato:
        return moeda(result)
    else:
        return result


def diminuir(num=0, porcentagem=0, formato=False):
    """
    -> Função para calcular um Desconto de Porcentagem
    :param num: Preço ou Número
    :param porcentagem: Quantidade da Desconto
    :param formato: {Opcional} True = Valor retorna formatado como uma moeda
    :return: O Preço após o desconto
    """
    result = num - (num * (porcentagem/100))
    if formato:
        return moeda(result)
    else:
        return result


def dobro(num=0, formato=False):
    """
    -> Função que Calcula o dobro de um número
    :param num: Número a ser calculado
    :param formato: {Opcional} True = Valor retorna formatado como uma moeda
    :return: O dobro do número
    """
    result = num * 2
    if formato:
        return moeda(result)
    else:
        return result


def metade(num=0, formato=False):
    """
    -> Função que Calcula a metade de um número
    :param num: Número a ser calculado
    :param formato: {Opcional} True = Valor retorna formatado como uma moeda
    :return: A metade do número
    """
    result = num / 2
    if formato:
        return moeda(result)
    else:
        return result


def resumo(num=0, aum=10, red=5):
    """
    -> Função que escreve uma Tabela com todas as informações presentes
    nesse módulo (Aumento, Desconto, Dobro e Metade)
    :param num: Número analisado
    :param aum: Porcentagem de aumento
    :param red: Porcentagem de desconto
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:'.ljust(20) + f'{moeda(num)}'.rjust(10))
    print(f'Dobro do preço:'.ljust(20) + f'{dobro(num, True)}'.rjust(10))
    print(f'Metade do preço:'.ljust(20) + f'{metade(num, True)}'.rjust(10))
    print(f'{aum}% de aumento:'.ljust(20) + f'{aumentar(num, aum, True)}'.rjust(10))
    print(f'{red}% de redução:'.ljust(20) + f'{diminuir(num, red, True)}'.rjust(10))
    print('-' * 30)
