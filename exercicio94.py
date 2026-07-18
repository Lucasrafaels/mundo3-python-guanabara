dados_pessoas = []
while True:
    pessoa = {}
    pessoa['Nome'] = input('Digite seu nome: ')
    pessoa['Idade'] = int(input('Digite sua idade: '))

    while True:
        sexo = input('Digite o seu sexo[M/F] ') .upper() .strip()
        if sexo in ('M', 'F'):
            break
        print('Opção inválida, digite "M" ou "F"!')
    pessoa['Sexo'] = sexo 

    dados_pessoas.append(pessoa)

    while True:
        continuar = input('Deseja continuar [S/N]? ') .upper() .strip()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida, digite "S" ou "N"!')
    if continuar == 'N':
        break
total_pessoas = len(dados_pessoas)

if total_pessoas > 0:
    soma_idade = sum(pessoa['Idade'] for pessoa in dados_pessoas)
    media_idades = soma_idade / total_pessoas

    mulheres = []
    for p in dados_pessoas:
        if p['Sexo'] == 'F':
            mulheres.append(p['Nome'])

    acima_media = []
    for p in dados_pessoas:
        if p['Idade'] > media_idades:
            acima_media.append(p['Nome'])

    print(f'A) Total de pessoas cadastradas: {total_pessoas}')
    print(f'B) Média de idade: {media_idades:.2f} anos')
    print(f'C) Mulheres cadastradas: {mulheres}')
    print(f'D) Pessoas com idade acima da média: {acima_media}')
else:
    print('Nenhuma pessoa cadastrada!')