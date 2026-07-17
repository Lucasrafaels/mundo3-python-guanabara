lista_valores = [[], []]
for numeros in range (0,7):
    numero_digitado = int(input(f'Digite o {numeros + 1}° número: '))
    if numero_digitado % 2 == 0:
        lista_valores[0].append(numero_digitado)
    else:
        lista_valores[1].append(numero_digitado)

print(f'A lista de números pares digitados em ordem crescente é {sorted(lista_valores[0])}')
print(f'A lista de números ímpares digitados em ordem crescente é {sorted(lista_valores[1])}')