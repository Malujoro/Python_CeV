def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos {aceita várias}
    :param sit: {Opcional} indica se deve ou não mostrar a situação do aluno
    :return: dicionário com várias informações sobre a situação do aluno
    Função criada por Mateus
    """
    print('-' * 30)
    aluno = dict()
    aluno['total'] = len(n)
    if len(n) == 0:
        aluno['maior'] = 0
        aluno['menor'] = 0
        aluno['média'] = 0
    else:
        aluno['maior'] = max(n)
        aluno['menor'] = min(n)
        aluno['média'] = sum(n) / len(n)
        if sit:
            if aluno['média'] >= 7:
                aluno['sit'] = 'BOA'
            elif aluno['média'] <= 5:
                aluno['sit'] = 'RUIM'
            else:
                aluno['sit'] = 'RAZOÁVEL'
    return aluno


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
# help(notas)
