#Criando uma classe de Pessoa
class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')
    
    def promover(self, novo_cargo):
        print(f'{self.nome} foi promovidada para a nova funcao {novo_cargo}!')

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando a idade de {self.idade} anos para {nova_idade} anos')
        else:
            print('A nova idade tem que ser maior que a antiga')

colaborador1 = Pessoa('Ana', 36, 'Assistente junior')
colaborador2 = Pessoa('Carlos', 25, 'Analista de T.I senior')


colaborador2.informacoes()
colaborador2.promover('Assistente Pleno')
colaborador2.atualizar_idade(54)