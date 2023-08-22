lin = '-=' * 20
times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense',
         'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG',
         'Goiás', 'Santos', 'Bragantino', 'Botafogo', 'São Paulo',
         'Ceará SC', 'Fortaleza', 'Coritiba', 'Cuiabá', 'Avaí',
         'Atlético-GO', 'Juventude')
print(f'{lin}\nLista de Times do Brasileirão:\n{times}\n{lin}')
print(f'5 Primeiros colocados:\n{times[:5]}\n{lin}')
print(f'4 Últimos colocados:\n{times[-4:]}\n{lin}')
print(f'Times em ordem alfabética:\n{sorted(times)}\n{lin}')
print(f'Corinthians está na {times.index("Corinthians") + 1}ª posição\n{lin}')
