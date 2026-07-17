lista_numeros = []
lista_pares = []
lista_impares = []
while True:
    numero_digitado = int(input('Digite um número para adicionar a lista: '))
    lista_numeros.append(numero_digitado)
    if numero_digitado % 2 == 0:
        lista_pares.append(numero_digitado)
    else:
        lista_impares.append(numero_digitado)
    while True:
        continuar = input('Deseja continuar[S/N]? ').strip() .upper()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida, digite "S" ou "N"!')
    if continuar == "N":
        break
print(f'A lista completa dos números digitados é: {lista_numeros}')
print(f'A lista de apenas os números pares digitados é: {lista_pares}')
print(f'A lista de apenas os números ímpares digitados é: {lista_impares}')