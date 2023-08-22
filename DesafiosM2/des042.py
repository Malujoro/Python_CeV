print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
