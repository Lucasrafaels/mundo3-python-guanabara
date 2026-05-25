lista_de_numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
                    'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                     'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
                     'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero_digitado = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero_digitado <= 20:
        print (f'Você digitou o número: {lista_de_numeros[numero_digitado]}')
        continuar = input('Deseja continuar [S/N]? ') .strip() .upper() [0]
        if continuar == 'N':
            print ('Programa encerrado')
            break
    else:
        print ('O número digitado está incorreto, tente novamente!')
