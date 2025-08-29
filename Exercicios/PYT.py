

#usuario = (input('Digite o seu usuario: '))
#senha = (input('Digite sua senha: '))

#if usuario == 'Admin' and senha == '123admin':
    #print('Login com sucesso')
#else:
    #print('Erro! Verifique o usuario e senha')


idade = int(input('Qual é sua idade: '))

if idade >= 18:
    print('Acesso ao sistema liberado')
elif idade >= 16:
    autorizado_pais = input('Voce tem autorização dos pais? (s/n): ')
    if autorizado_pais == 's':
        print('Acesso liberado com autorização dos pais')
    else:
        print('Acesso negado')
else:
    print('Acesso negado')