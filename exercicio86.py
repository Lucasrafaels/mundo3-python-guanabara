numeros_matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linhas in range (0,3):
    for colunas in range (0,3):
        numeros_matriz [linhas][colunas] = int(input(f'Digite um número para {linhas}, {colunas}: '))
for linhas in range (0,3):
    for colunas in range (0,3):
        print(f'[{numeros_matriz[linhas][colunas]}]', end = '')
    print()