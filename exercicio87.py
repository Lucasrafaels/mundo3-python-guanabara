numeros_matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = maior_valor = soma_coluna = 0
for linhas in range (0,3):
    for colunas in range (0,3):
        numeros_matriz [linhas][colunas] = int(input(f'Digite um número para {linhas}, {colunas}: '))
for linhas in range (0,3):
    for colunas in range (0,3):
        print(f'[{numeros_matriz[linhas][colunas]}]', end = '')
        if numeros_matriz[linhas][colunas] % 2 == 0:
            soma_pares += numeros_matriz[linhas][colunas]
    print()
print(f'A soma dos valores pares é igual a {soma_pares}')
for linhas in range (0,3):
    soma_coluna += numeros_matriz[linhas][2]
print(f'A soma de todos os valores da terceira coluna é igual a {soma_coluna}')
for coluna in range (0,3):
    if coluna == 0:
        maior_valor = numeros_matriz[1][coluna]
    elif numeros_matriz[1][coluna] > maior_valor:
        maior_valor = numeros_matriz[1][coluna]
print(f'o maior valor na segunda linha é {maior_valor}')