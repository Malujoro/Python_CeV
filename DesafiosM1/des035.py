print('\033[35m-=\033[m' * 20)
print('\033[31mAnalisador de Triângulos\033[m')
print('\033[35m-=\033[m' * 20)
n1 = float(input('\033[33mPrimeiro Segmento:\033[m '))
n2 = float(input('\033[36mSegundo Segmento:\033[m '))
n3 = float(input('\033[34mTerceiro Segmento:\033[m '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m triângulo')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo')
