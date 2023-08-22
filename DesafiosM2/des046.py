from time import sleep
from emoji import emojize
input('CONTAGEM PARA OS FOGOS DE ARTIFÍCIO')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(f'{emojize(":rocket:")} BOOOOM {emojize(":rocket:")}')
