from datetime import date
atual = date.today().year
ficha = {'nome': str(input('Nome: ').capitalize()),
         'idade': atual - int(input('Ano de nascimento: ')),
         'ctps': int(input('Carteira de Trabalho: (0 não tem): '))}
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = (ficha['contratação'] + 35) - (atual - ficha['idade'])
print('-=' * 40)
for k, v in ficha.items():
    print(f'  > {k.capitalize()} tem o valor {v}')
