lista_valores = list()
maior_valor = 0
menor_valor = 0
for posicao in range (0,6):
    lista_valores.append(int(input(f'Digite o valor para a posição {posicao}: ')))
    if posicao == 0:
        maior_valor = menor_valor = lista_valores[posicao]
    else:
        if lista_valores[posicao] > maior_valor:
            maior_valor = lista_valores[posicao]
        if lista_valores[posicao] < menor_valor:
            menor_valor = lista_valores[posicao]
print ('=' * 50)
print (f'OS valores digitados foram: {lista_valores}')
print (f'O maior valor digitado foi: {maior_valor} na posição {lista_valores.index(maior_valor)}')
print(f'O menor valor digitado foi: {menor_valor} na posição {lista_valores.index(menor_valor)}')