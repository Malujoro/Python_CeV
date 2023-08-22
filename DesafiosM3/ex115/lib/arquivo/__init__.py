from DesafiosM3.ex115.lib.interface import cor, cabecalho


def arquivo_existe(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'{cor(nome, "roxo")} {cor("criado com sucesso!!", "verde")}')


def ler_arquivo(arquivo):
    try:
        dados = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in dados:
            separado = linha.split(';')
            separado[1] = separado[1].replace('\n', '')
            print(f'{separado[0]:<38}{separado[1]:>3} anos')
        dados.close()


def cadastrar(arquivo, nome='desconhecido', idade='0'):
    try:
        banco = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            banco.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo Registro de {nome} adicionado.')
        finally:
            banco.close()
