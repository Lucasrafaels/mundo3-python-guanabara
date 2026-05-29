valores_digitados = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
                     int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print (f'O número 9 apareceu {valores_digitados.count(9)} vezes.')
if 3 in valores_digitados:
    print(f'O número 3 apareceu na {valores_digitados.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
numeros_pares = 0
for numeros in valores_digitados:
    if numeros % 2 == 0:
        numeros_pares += 1
print (f'Foram digitados {numeros_pares} valores pares.')