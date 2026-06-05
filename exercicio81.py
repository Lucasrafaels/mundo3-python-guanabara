lista_numeros = list()
while True:
    numero_digitado = int(input('Digite um valor: '))
    lista_numeros.append(numero_digitado)
    continuar = input('Deseja continuar [S/N]? ') .strip() .upper()
    if continuar.startswith('N'):
        break
print (f'Você digitou {len(lista_numeros)} valores')
print(f'Os valores digitados em forma decrescente são {sorted(lista_numeros, reverse=True)}')
if 5 in lista_numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')