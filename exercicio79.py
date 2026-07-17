lista_numeros = []
while True:
    numero_digitado = int(input('Digite um número para adicionar a uma lista: '))
    if numero_digitado not in lista_numeros:
        lista_numeros.append(numero_digitado)
    else:
        print('Este número já foi digitado')
    while True:
        continuar = input('Deseja continuar [S/N]? ') .upper() .strip()
        if continuar in ('S', 'N'):
            break
        print ('Opção inválida, digite "S" ou "N"!')
    if continuar == 'N':
        break
print (f'Os números digitados em ordem crescente foram: {sorted(lista_numeros)}')