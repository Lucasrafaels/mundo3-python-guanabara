lista_numeros = []
while True:
    numero_digitado = int(input('Digite um número para adicionar a lista: '))
    lista_numeros.append(numero_digitado)
    while True: 
        continuar = input('Desejar continuar [S/N]? ') .strip() .upper()
        if continuar in ('S', 'N'):
            break
        print ('Opção inválida, digite "S" ou "N"!')
    if continuar == 'N':
        break
print(f'Você digitou {len(lista_numeros)} valores')
print(f'A sua lista em ordem decrescente é: {sorted(lista_numeros, reverse = True)}')   
if 5 in lista_numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')














































# lista_numeros = list()
# while True:
#     numero_digitado = int(input('Digite um valor: '))
#     lista_numeros.append(numero_digitado)
#     continuar = input('Deseja continuar [S/N]? ') .strip() .upper()
#     if continuar.startswith('N'):
#         break
# print (f'Você digitou {len(lista_numeros)} valores')
# print(f'Os valores digitados em forma decrescente são {sorted(lista_numeros, reverse=True)}')
# if 5 in lista_numeros:
#     print('O valor 5 faz parte da lista!')
# else:
#     print('O valor 5 não foi encontrado na lista.')