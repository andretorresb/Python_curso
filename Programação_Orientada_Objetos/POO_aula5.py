class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome} e tenho {self.idade} de idade')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        self.cargo = cargo

    def trabalhar(self):
        print('{}')

class Cliente(Pessoa):
    pass

pessoa1 = Pessoa('Andre', 13)
pessoa1.apresentar()

cliente1 = Cliente('Yasmin', 16)

