def voto(ano=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 15:
        result = 'NÃO VOTA'
    elif 18 <= idade < 65:
        result = 'VOTO OBRIGATÓRIO'
    else:
        result = 'VOTO OPCIONAL'
    return f'Com {idade} anos: {result}.'


# Programa Principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
