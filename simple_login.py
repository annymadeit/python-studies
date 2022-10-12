registro_user = {
    'nome' : input('Digite seu nome: '),
    'sobrenome' : input('Digite seu sobrenome: '),
    'idade' : int(input('Digite sua idade: ')),
    'genero' : input('Informe seu gênero: ')
}
genero = (registro_user['genero'])

if (genero == 'feminino'):
    print('Bem vinda, ' + registro_user['nome'] + ' ' + registro_user['sobrenome'])
elif (genero == 'masculino'):
    print('Bem vindo, ' + registro_user['nome'] + ' ' + registro_user['sobrenome'])
else:
    print('Por favor, tente novamente.')
