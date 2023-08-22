def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: {opcional} Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    fat = 1
    print('-' * 30)
    for n in range(num, 0, -1):
        fat *= n
        if show:
            print(n, end='')
            if n > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return fat


# Programa Principal
print(fatorial(5, show=False))
print(fatorial(5, show=True))
#help(fatorial)
