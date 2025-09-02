usuario = input('Digite seu Usuario: ')
senha = input('Digite sua senha: ')

if usuario == 'Admin' and senha == '123admin':
    print('Login efetuado com sucesso!')
elif usuario != 'Admin' and senha != '123admin':
    print('usuario e senha incorreto')
elif usuario != 'Admin':
    print('usuario incorreto')
elif senha != '123admin':
    print('senha incorreto')