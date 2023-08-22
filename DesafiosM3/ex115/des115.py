from DesafiosM3.ex115.lib.interface import *
from DesafiosM3.ex115.lib.arquivo import *
from time import sleep

arq_nome = 'CursoVideo.txt'

if arquivo_existe(arq_nome):
    print(f'{cor("Arquivo encontrado com sucesso!", "verde")}')
else:
    print(f'{cor("Arquivo não encontrado!", "vermelho")}')
    criar_arquivo(arq_nome)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        ler_arquivo(arq_nome)
    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leia_int('Idade: ')
        cadastrar(arq_nome, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'{cor("ERRO! Digite uma opção válida", "vermelho")}')
    sleep(1)
