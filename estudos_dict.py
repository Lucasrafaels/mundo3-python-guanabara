pessoas = {'Nome': 'Lucas', 'Idade': 20, 'Sexo': 'M'}
print('-='*20)
print(f'O {pessoas['Nome']} tem {pessoas["Idade"]} anos!')
print(pessoas.keys())
print(pessoas.values())
print('-='*20)
for k in pessoas.keys():
    print(k)
print('-='*20)
pessoas['Peso'] = 78
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*20)  
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'Minas Gerais', 'Sigla': 'MG'}
brasil += [estado1, estado2]
print(brasil[1])
print('-='*20)  
estado = {}
brasil = []
for c in range (0,3):
    estado['UF'] = input('Digite o Seu estado: ')
    estado['Sigla'] = input('Digite a sigla do seu estado: ')
    brasil.append(estado.copy())
print(estado["UF"])