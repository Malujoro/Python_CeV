lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    # Primeiro loop: adiciona um número
    # ou Adiciona N na última posição
    if c == 0 or n >= lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for p, v in enumerate(lista):
            # Identifica que posição deve colocar N
            if n < lista[p]:
                lista.insert(p, n)
                print(f'Adicionando na posição {p} da lista...')
                break
print('-=' * 20)
print(f'Os valores digitados em ordem foram: {lista}')
