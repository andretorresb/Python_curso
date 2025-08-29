from funcoes import verificar_maioridade

minha_idade = int(input('Digita a sua idade: '))

if verificar_maioridade(minha_idade):
    print('Voce e maior de idade: ')
else:
    print('Voce é menor de idade')