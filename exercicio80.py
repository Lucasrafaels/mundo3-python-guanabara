lista_numeros = []
for valores in range (0,5):
    numero_digitado = int(input(f'Digite um valor na posição {valores}: '))
    posicao_lista = 0
    while posicao_lista < len(lista_numeros) and lista_numeros[posicao_lista] < numero_digitado:
        posicao_lista += 1
    lista_numeros.insert(posicao_lista, numero_digitado)
    print(f"O número {numero_digitado} foi inserido na posição {posicao_lista}.")
print("\nLista ordenada (crescente):", lista_numeros)