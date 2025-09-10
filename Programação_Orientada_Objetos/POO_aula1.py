#CLASSE
class Casa:           
  
  #ATRIBUTOS
  def __init__(self, cor, quartos, banheiros):         
    self.cor = cor
    self.quartos = quartos
    self.banheiros = banheiros

 #MÉTODOS
  def mostrar_cor(self):
    print(f'A cor da casa é {self.cor}')

  def mostrar_quartos(self):
    print(f'Essa casa tem {self.quartos} quartos')

  def mostrar_banheiros(self):
    print(f'Essa casa tem {self.banheiros} banheiros')

  def adicionar_quarto(self):
    self.quartos += 1
    print(f'Agora essa casa tem {self.quartos} quartos')

#ADICIONANDO VALORES NO ATRIBUTOS 
casa1 = Casa('Azul', 2, 3)
casa2 = Casa('Amarela', 5, 2)

#INSTANCIA
print('\nCasa 1:')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()

print('\nCasa 2:')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()