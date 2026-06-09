lista_numeros = list()
numeros_pares = []
numeros_impares = []
while True:
    numero_digitado = int(input('Digite um número: '))
    lista_numeros.append(numero_digitado)
    if numero_digitado % 2 == 0:
        numeros_pares.append(numero_digitado)
    else:
        numeros_impares.append(numero_digitado)
    continuar = input('Deseja continuar [S/N]? ') .strip() .upper()
    if continuar.startswith('N'):
        break
print(f'A sua lista de números é {lista_numeros}')
print(f'OS número pares são {numeros_pares}')
print(f'Os números ímpares são {numeros_impares}')