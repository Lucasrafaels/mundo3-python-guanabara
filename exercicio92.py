from datetime import datetime
ano_atual = datetime.now().year
cadastro = {}
cadastro['Nome'] = input('Digite seu nome completo: ')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
cadastro['Idade'] = ano_atual - ano_nascimento
cadastro['CTPS'] = int(input('Digite o número da sua carteira de trabalho (Digite 0 caso não tenha): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Digite seu ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o seu salário: R$'))
    tempo_contribuicao = ano_atual - cadastro['Ano de contratação']
    if tempo_contribuicao >= 35:
        cadastro['Idade de aposentadoria'] = cadastro['Idade']
    else:
        anos_faltando = 35 - tempo_contribuicao
        cadastro['Idade de aposentadoria'] = cadastro['Idade'] + anos_faltando
for k, v in cadastro.items():
    print(f'{k} - {v}')
