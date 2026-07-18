time = []
dados_jogador = {}  

while True:
    dados_jogador.clear() 
    dados_jogador['Nome'] = input('Digite o nome do jogador: ')
    dados_jogador['Partidas'] = int(input('Digite a quantidade de partidas: '))
    dados_jogador['Gols por partida'] = []

    for i in range(dados_jogador['Partidas']):
        gols = int(input(f'digite quantos gols foram no {i+1}° jogo: '))
        dados_jogador['Gols por partida'].append(gols)
        
    dados_jogador['Total de gols'] = sum(dados_jogador['Gols por partida'])

    time.append(dados_jogador.copy())  

    while True:
        continuar = input('Deseja continuar [S/N]? ').upper().strip()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida, digite "S" ou "N"!')
    if continuar == 'N':
        break

print('\n' + '='*30)
print('RESUMO DE TODOS OS JOGADORES')
print('='*30)

for i, jogador in enumerate(time, start=1):
    print(f'\n--- Jogador {i}: {jogador["Nome"]} ---')
    print(f'Partidas: {jogador["Partidas"]}')
    print(f'Total de gols: {jogador["Total de gols"]}')
    print('Gols por partida:')
    for j, gols in enumerate(jogador['Gols por partida'], start=1):
        print(f'  Jogo {j}: {gols} gol(s)')