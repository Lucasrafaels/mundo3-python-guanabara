lista_times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino',
               'São Paulo', 'Coritiba', 'Bahia', 'Cruzeiro', 'Botafogo',
               'Vitória', 'Atlético-MG', 'Internacional','Grêmio', 'Corinthians',
               'Vasco', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')
print ('='*100)
print (f'Lista dos 20 times  do brasileirão 2026 na rodada 17: {lista_times}')
print ('='*100)
print (f'Os cinco primeiros são:{lista_times[0:5]}')
print ('='*100)
print (f'Os times em ordem alfabética são {sorted(lista_times)}')
print ('='*100)
print (f'A posição do Fluminense é {(lista_times.index("Fluminense")) + 1}')
print ('='*100)