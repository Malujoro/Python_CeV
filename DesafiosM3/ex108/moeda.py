def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(num=0, porcentagem=0):
    """
   -> Função para calcular um Aumento de Porcentagem
    :param num: Preço ou Número
    :param porcentagem: Quantidade do Aumento
    :return: O Preço após o aumento
    """
    result = num + (num * (porcentagem / 100))
    return result


def diminuir(num=0, porcentagem=0):
    """
    -> Função para calcular um Desconto de Porcentagem
    :param num: Preço ou Número
    :param porcentagem: Quantidade da Desconto
    :return: O Preço após o desconto
    """
    result = num - (num * (porcentagem/100))
    return result


def dobro(num=0):
    """
    -> Função que Calcula o dobro de um número
    :param num: Número a ser calculado
    :return: O dobro do número
    """
    result = num * 2
    return result


def metade(num=0):
    """
    -> Função que Calcula a metade de um número
    :param num: Número a ser calculado
    :return: A metade do número
    """
    result = num / 2
    return result
