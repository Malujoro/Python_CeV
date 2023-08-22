from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        print('ERRO! passo nulo foi convertido para 1')
    # Transforma o "Pulo" negativo em positivo, para mostrar no interface
    elif passo < 0:
        passo = -passo
    # Menu
    print('-=' * 25)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    # Transforma o "Pulo" em negativo caso identifique contagem regressiva
    if inicio > fim and passo > 0:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    # Contagem
    for n in range(inicio, fim, passo):
        sleep(0.3)
        print(f'{n} ', end='')
    sleep(0.3)
    print(f'FIM!')


# Programa Principal
# contador(1, 10, 1)
# contador(10, 0, 2)
print('-=' * 25)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
