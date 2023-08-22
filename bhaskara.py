from math import sqrt


def bhask():
    print('''Calculadora de Bháskara
Digite os valores de:''')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    delta = (b**2) - (4 * a * c)
    print('O valor de Delta é {}'.format(delta))
    if delta < 0:
        print('Não é possível continuar, pois Delta é negativo')
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        if delta == 0:
            print('''Delta tem apenas UMA raiz
    O valor de X é {:.2f}'''.format(x1))
        elif delta > 0:
            print('''Delta tem DUAS raízes 
    Os valores de X são: {:.2f} e {:.2f}'''.format(x1, x2))


bhask()
