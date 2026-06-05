lista_numeros = list()
for contagem_numeros in range (0,5):
    numeros_digitados = int(input('Digite um valor: '))
    if contagem_numeros == 0 or numeros_digitados > lista_numeros[-1]:
        lista_numeros.append(numeros_digitados)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista_numeros):
            if numeros_digitados <= lista_numeros[posicao]:
                lista_numeros.insert(posicao,numeros_digitados)
                print(f'Adicionado a posição {posicao+1} da lista')
                break
            posicao += 1
print('='*50)
print(f'Os valores digitados em ordem crescente {lista_numeros}')