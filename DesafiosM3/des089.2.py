lista = []
# Lista [ [ Nome, [ Nota 1, Nota 2 ], Média ] ]
lin = ['-' * 30, '-=' * 20, '-' * 60]

while True:
    # Coleta nome, nota 1, nota 2 e média e os adiciona na lista
    while True:
        nome = str(input('Nome: ')).strip().capitalize()
        if nome != '':
            break
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    # Tratamento da resposta de "Continuar"
    while True:
        cont = str(input('Continuar? [S/N] ')).strip().upper()
        if cont != '':
            if cont in 'SN':
                break
    if cont in 'N':
        break
# Menu do boletim
print(lin[1])
print(f'{"Nº":<4}{"NOME":<18}{"MÉDIA":>5}')
print(lin[0])
# Mostra o código, nome e média do aluno
for cod, a in enumerate(lista):
    print(f'{cod:<4}{a[0]:<18}{a[2]:>5.1f}')
print(lin[0])
# Mostra as notas do aluno que o código for digitado
while True:
    n = input('Mostrar notas de qual aluno? [Enter para interromper]: ')
    if n == '':
        break
    else:
        cod = int(n)
        if 0 <= cod <= len(lista)-1:
            print(f'Notas de {lista[cod][0]} são {lista[cod][1]}')
        else:
            print('Aluno não cadastrado')
        print(lin[2])
# Tela final
print(f'{lin[2]}\n'
      'FINALIZANDO...\n' +
      '<' * 5 + ' VOLTE SEMPRE ' + '>' * 5)
