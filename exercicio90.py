from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)}
ranking = []
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k} recebeu o número {v} no dado')
print('-='* 20)
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos!')
    sleep(1)