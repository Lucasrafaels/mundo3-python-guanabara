lista_palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 
            'mercado', 'programar', 'futuro')
for palavra in lista_palavras:
    print(f'\nNa palavra "{palavra}" temos as vogais: ' , end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
