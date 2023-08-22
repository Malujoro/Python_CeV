lista = []  # Lista [ [ Aluno ] ]
aluno = []  # Aluno [ Nome, [ Notas ], [ Média ] ]
notas = []  # Notas [ N1, N2 ]
media = []
lin = ['-' * 30, '-=' * 20, '-' * 60]

while True:
    while True:
        # Recebe o nome e adiciona no ALUNO
        nome = str(input('Nome: ')).strip().capitalize()
        if nome != '':
            break
    aluno.append(nome)
    # Recebe as notas e adiciona em NOTAS
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    # Calcula a média e adiciona em MÉDIA
    medias = (n1 + n2) / 2
    media.append(medias)
    # Adiciona as NOTAS e as MÉDIAS dentro dos dados do ALUNO
    aluno.append(notas[:])
    notas.clear()
    aluno.append(media[:])
    media.clear()
    # Adiciona o ALUNO na lista principal
    lista.append(aluno[:])
    aluno.clear()
    # Tratamento da resposta de "Continuar"
    while True:
        cont = str(input('Continuar? [S/N] ')).strip().upper()
        if cont != '':
            if cont[0] in 'SN':
                break
    if cont in 'N':
        break
# Menu do boletim
print(lin[1])
print(f'{"Nº":<4}{"NOME":<15}{"MÉDIA":>5}')
print(lin[0])
# Mostra o código, nome e média do aluno
for c in range(0, len(lista)):
    print(f'{c:<4}{lista[c][0]:<15}{lista[c][2][0]:>5.1f}')
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
