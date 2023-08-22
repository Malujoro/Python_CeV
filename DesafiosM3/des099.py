from time import sleep
lin = '-=' * 30


def maior(* num):
    mai = 0
    print(f'{lin}\nAnalisando os valores passados...')
    print('[ ', end='')
    for i, n in enumerate(num):
        sleep(0.3)
        print(n, end=' ')
        # Descobre o maior
        if i == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(']', end=' ')
    sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.\n'
          f'O maior valor informado foi {mai}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
