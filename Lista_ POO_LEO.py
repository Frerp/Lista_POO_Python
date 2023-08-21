from math import sqrt

print("-------------- Questão 1 --------------")

class Produto:

  descricao = "produto de informatica"; 
  
  def __init__(self, nomeloja, preco):
    self.preco = preco #eita como priva
    self.nomeloja = nomeloja #privadohhh

  @property
  def define_preco(self):
    return self.__preco

  @define_preco.setter
  def preco(self,novo_preco):
    self.__preco = float(novo_preco)

  @property
  def define_nomeloja(self):
    return self.__nomeloja

  @define_nomeloja.setter
  def nomeloja(self, novo_nomeloja):
    self.__nomeloja = novo_nomeloja
    
    
produto = Produto("farinha lima",32)
print(produto.preco)
produto.preco = 31
print(produto.preco)
produto.nomeloja = "farinha - lima"
print(produto.nomeloja)


print("-------------- Questão 2 --------------")

class Retangulo:
  
  def __init__(self, altura, largura):
    self.altura = altura
    self.largura = largura

  @property
  def define_largura(self):
    return self.__largura

  @define_largura.setter
  def largura(self, nova_largura):
    self.__largura = float(nova_largura)

  @property
  def define_altura(self):
    return self.__altura

  @define_altura.setter
  def altura(self, nova_altura):
    self.__altura = nova_altura

  def hipotenusa(self,largura, altura):
    return sqrt(largura**2 + altura**2)
