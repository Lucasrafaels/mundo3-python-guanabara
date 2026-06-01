lista_valores = list()
while True:
    numeros_digitados = int(input('Digite um valor: '))
    if numeros_digitados not in lista_valores:
        lista_valores.append(numeros_digitados)
    else:
        print ('Esse valor já foi digitado!')
    resposta = input('Deseja continuar?[S/N]: ') .strip() .upper()
    if resposta.startswith ('N'):
        break
print (f'Os valores digitados foram {sorted(lista_valores)}')