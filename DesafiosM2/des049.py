print('TABUADA')
n = int(input('Você quer a tabuada de qual número?: '))
f = int(input('Qual a multiplicação final?: '))
print('-=' * 10)
for c in range(1, f+1):
    print(f'{n} x {c:2} = {n * c}')
