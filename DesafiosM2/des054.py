from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'{c}º ano de nascimento: '))
    if atual - ano >= 21:
        maior += 1
    elif atual - ano < 21:
        menor += 1
print(f'''Maioridade: 21 anos | Ano: {atual}
De 7 pessoas:
| {maior} já atingiram a maioridade
| {menor} não atingiram a maioridade''')
