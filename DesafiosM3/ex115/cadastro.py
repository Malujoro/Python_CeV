linha = '-' * 50
cor = {'base': '\033[m',
       'vermelho': '\033[31m',
       'amarelo': '\033[33m',
       'azul': '\033[34m'}


def menu():
    print(linha)
    print('MENU PRINCIPAL'.center(50))
    print(linha)
    print(f'{cor["amarelo"]}1 - {cor["azul"]}Ver pessoas cadastradas{cor["base"]}')
    print(f'{cor["amarelo"]}2 - {cor["azul"]}Cadastrar nova Pessoa{cor["base"]}')
    print(f'{cor["amarelo"]}3 - {cor["azul"]}Sair do Sistema{cor["base"]}')
    while True:
        print(linha)
        try:
            op = str(input(f'{cor["amarelo"]}Sua Opção:{cor["base"]} ')).strip()
            op = int(op)
        except:
            print(f'{cor["vermelho"]}ERRO! Digite um número inteiro válido{cor["base"]}')
        else:
            if 1 <= op <= 3:
                return op
            else:
                print(f'{cor["vermelho"]}ERRO! Digite uma opção válida{cor["base"]}')
                break


def lista():
    dados = open('pessoas.txt', 'r')
    print(linha)
    print('PESSOAS CADASTRADAS'.center(50))
    print(linha)
    pessoas = dados.readlines()
    for pes in pessoas:
        print(f'{pes}', end='')


def pessoa():
    arquivo = open('pessoas.txt', 'a+')
    print(linha)
    print('NOVO CADASTRO'.center(50))
    print(linha)
    nome = str(input('Nome: ')).strip().title()
    while True:
        try:
            idade = str(input('Idade: ')).strip()
            idade = int(idade)
            break
        except:
            print(f'{cor["vermelho"]}ERRO! Digite um número inteiro válido {cor["base"]}')
    arquivo.write(f'{nome:<38}{idade} anos')
    arquivo.write('\n')
    print(f'Novo Registro de {nome} adicionado.')
    arquivo.close()


def fim():
    print(linha)
    print('Saindo do sistema... Até logo!'.center(50))
    print(linha)
