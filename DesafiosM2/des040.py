n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média é {:.1f}'.format(media))
if media < 5.0:
    print('O aluno está {}REPROVADO'.format('\033[0;31m'))
elif 5.0 <= media <= 6.9:
    print('O aluno está de {}RECUPERAÇÃO'.format('\033[0;36m'))
else:
    print('O aluno está {}APROVADO'.format('\033[0;32m'))
