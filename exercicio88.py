from random import randint
print('=' * 30)
print('Jogo da mega sena')
print('=' * 30)
numero_jogos = int(input('Digite quantos jogos deseja jogar; '))
lista_jogos = []
for jogos in range(numero_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:           
           jogo.append(numero)
    jogo.sort()
    lista_jogos.append(jogo)
for indice, jogo in enumerate(lista_jogos):
    print(f'Jogo {indice + 1}: {jogo}')