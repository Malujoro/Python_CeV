lin = '-' * 35
while True:
    # c = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(lin)
    if n < 0:
        break
    # while c <= 10:
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    #     c += 1
    print(lin)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
