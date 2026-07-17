ficha = []
while True:
    nome_aluno = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome_aluno, nota1, nota2, media])
    while True:
        continuar = input('Deseja continuar [S/N]: ') .strip() .upper()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida, tente "S ou "N"! ')
    if continuar == 'N':
        break
for indice, aluno in enumerate(ficha):
    print(f'{indice+1:2d}. {aluno[0]:15s} Média: {aluno[3]:.2f}')
while True:
    escolha_aluno = int(input('Mostrar nota de qual aluno [999 para encerrar]?: '))
    if escolha_aluno == 999:
        print('Fim do programa!')
        break
    indice = escolha_aluno - 1
    if 0 <= indice < len(ficha):
        nome = ficha[indice][0]
        nota1 = ficha[indice][1]
        nota2 = ficha[indice][2]
        print(f'As notas de {nome} são {nota1} e {nota2}')
    else:
        print('Número inválido. Tente novamente.')