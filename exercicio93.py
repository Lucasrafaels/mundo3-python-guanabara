dados_jogador = {}
dados_jogador['Nome'] = input('Digite o nome do jogador: ')
dados_jogador['Partidas'] = int(input('Digite a quantidade de partidas: '))
dados_jogador['Gols por partida'] = []

for i in range (dados_jogador['Partidas']):
  gols = int(input(f'digite quantos gols foram no {i+1}° jogo: '))
  dados_jogador['Gols por partida'].append(gols)

dados_jogador['Total de gols'] = sum(dados_jogador['Gols por partida'])

for k, v in dados_jogador.items():
    print(f'{k} - {v}')
for i, gols in enumerate(dados_jogador['Gols por partida']):
   print(f'No {i+1}° jogo o jogador fez {gols} gols')