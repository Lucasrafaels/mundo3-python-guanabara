lista_pessoas = []
maior_peso = 0
menor_peso = 0
while True:
    nome_pessoa = input('Digite o seu nome: ') .strip()
    peso_pessoa = float(input('Digite o seu peso em kg: '))
    if len(lista_pessoas) == 0:
        maior_peso = menor_peso = peso_pessoa
    else:
        if peso_pessoa > maior_peso:
            maior_peso = peso_pessoa
        if peso_pessoa < menor_peso:
            menor_peso = peso_pessoa
    lista_pessoas.append((nome_pessoa, peso_pessoa))
    while True:
        continuar = input('Deseja continuar[S/N]? ') .strip() .upper()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida, digite "S" ou "N"! ')
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(lista_pessoas)} pessoas! ')
print(f'O maior peso foi de {maior_peso} kg')
for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]}')
print(f'O menor peso foi de {menor_peso}Kg')
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}')