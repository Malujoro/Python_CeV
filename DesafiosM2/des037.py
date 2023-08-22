n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[1] para Binário\n'
      '[2] para Octal\n'
      '[3] para Hexadecimal')
base = int(input('Sua opção: '))
if base == 1:
    print('{} em Binário é {}'.format(n, bin(n)[2::]))
elif base == 2:
    print('{} em Octal é {}'.format(n, oct(n)[2::]))
elif base == 3:
    print('{} em Hexadecimal é {}'.format(n, hex(n)[2::]))
else:
    print('Desculpe, base de conversão não reconhecida')
