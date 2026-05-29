lista_produtos  = ('Lápis', 1.75,
                   'Borracha', 2,
                   'Caderno',15.90,
                   'Estojo',25,
                   'Transferidor', 4.20,
                   'Compasso', 9.99,
                   'Mochila', 120.32,
                   'Canetas',22.30,
                   'Livro',34.90)
print('='*50)
print (f'{'Papelaria':^40}')
print('='*50)
for posicao in range (0,len(lista_produtos)):
    if posicao % 2 == 0:
        print (f'{lista_produtos[posicao]:.<30}', end = '')
    else:
        print(f'R${lista_produtos[posicao]:>5.2f}')
print('='*50)