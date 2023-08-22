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
