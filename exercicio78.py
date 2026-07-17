lista_numeros = []
maior_numero = menor_numero = 0
for posicao in range (0,5):
    lista_numeros.append(int(input(f'Digite um número para adicionar a lista na posição {posicao + 1}: ')))
    if posicao == 0:
        maior_numero = menor_numero = lista_numeros[posicao]
    else:
        if lista_numeros[posicao]>maior_numero:
            maior_numero = lista_numeros[posicao]
        if lista_numeros[posicao] < menor_numero:
            menor_numero = lista_numeros[posicao]
print ('=' * 50)
print(f'Os valores digitados foram: {lista_numeros}')
print(f'O maior valor digitado foi: {maior_numero} na posição {lista_numeros.index(maior_numero)+1}')
print(f'O menor valor digitado foi: {menor_numero} na posição {lista_numeros.index(menor_numero)+1}')
print ('=' * 50)