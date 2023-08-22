print('Detector de Palíndromo')
# Aumenta todas as letras, corta todos os espaços e junta em uma palavra
frase = (''.join(input('Insira uma frase: ').upper().split()))
tamanho = int(len(frase)) - 1  # diminui 1 por causa da posição 0
frase2 = frase[::-1]
# frase2 = ''
# for c in range(tamanho, -1, -1):  # monta a palavra inversa
#     frase2 += frase[c]
print(f'O inverso de {frase} é {frase2}')

if frase == frase2:  # confere se é um palíndromo
    palin = 'É'
else:
    palin = 'NÃO É'

print(f'A frase {palin} um PALÍNDROMO')
