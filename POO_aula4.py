#HERANÇA COM ANIMAIS
#class PAI
class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou o(a) {self.especie} chamado(a) {self.nome}')

#HERANÇA - class FILHO   
class Gato(Animal):
    def emitir_som(self):
        print(f'MIAU!')

    def arranhar(self):
        print('O gato esta arranhando :(')    

class  Cachorro(Animal):
    def emitir_som(self):
        print(f'AU AU AU...')

class  Elefante(Animal):
    def emitir_som(self):
        print(f'Pruuuuuu....')
    

gato1 = Gato('Felix', 'Vermelho', 'Siamese cat')
gato1.apresentar()
gato1.emitir_som()
gato1.arranhar()

cachorro1 = Cachorro('Russo', 'Preto', 'Pastor Alemao')
cachorro1.apresentar()
cachorro1.emitir_som()

elefante1 = Elefante('Frede', 'Marrom', 'Asiatico')
elefante1.apresentar()
elefante1.emitir_som()