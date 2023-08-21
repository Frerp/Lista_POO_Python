from math import sqrt

#QUESTÃO 1
class Produto:
  descricao = "Produto de informática"

  def __init__(self, nomeloja, preco):
    self.nomeloja = nomeloja
    self.preco = preco

  @classmethod
  def getDescricao(cls):
    return cls.descricao

  @property
  def nome_da_loja(self): # nome da propriedade que vai passar pelo setter
    return self._nomeloja

  @nome_da_loja.setter # o nome da propriedade tem que ser igual no setter
  def nomeloja(self, valor):
    """ A função definida no setter tem que ter o mesmo
    nome do atributo de instância para que o setter possa de fato filtrar o
    valor atribuído ao atributo de instância"""
    self._nomeloja = valor.title()

  @property
  def preco_do_produto(self):
    return self._preco

  @preco_do_produto.setter
  def preco(self, valor):
    valor = float(valor)
    self._preco = valor

print("\n---------------Questão 1---------------")
produto1 = Produto("informHouse variedades", 45)
print(Produto.getDescricao())
print(f"Nome da loja: {produto1.nomeloja}")
print(f"preco do produto: R${str(produto1.preco)}")


#QUESTÃO 2
class Retangulo():

  def __init__(self, altura, largura):
    self.altura = altura
    self.largura = largura

  def atribuir_altura(self):
    altura = float(input("Digite o valor de altura do retângulo: "))
    self.altura = altura

  def atribuir_largura(self):
    largura = float(input("Digite o valor de largura do retângulo: "))
    self.largura = largura

print("\n---------------Questão 2---------------")
retangulo1 = Retangulo(15, 25)
print(f"altura do retangulo1: {retangulo1.altura}")
print(f"largura do retangulo1: {retangulo1.largura}")
retangulo1.atribuir_altura()
retangulo1.atribuir_largura()
print(f"altura do retangulo1: {retangulo1.altura}")
print(f"largura do retangulo1: {retangulo1.largura}")


#QUESTÃO 3
class Trianguloretangulo():

  def __init__(self):
    self.catetobase = 0
    self.catetoaltura = 0
    self.hipotenusa = 0

  def atribuir_catetobase(self):
    catetobase = float(input("Digite o valor do cateto base: "))
    self.catetobase = catetobase

  def atribuir_catetoaltura(self):
    catetoaltura = float(input("Digite o valor do cateto altura: "))
    self.catetoaltura = catetoaltura

  def calcula_hipotenusa(self):
    self.hipotenusa = sqrt(self.catetobase**2 + self.catetoaltura**2)

print("\n---------------Questão 3---------------")
trianguloretangulo1 = Trianguloretangulo()
trianguloretangulo1.atribuir_catetobase()
trianguloretangulo1.atribuir_catetoaltura()
trianguloretangulo1.calcula_hipotenusa()
print(f"Valor do cateto base: {trianguloretangulo1.catetobase}")
print(f"Valor do cateto altura: {trianguloretangulo1.catetoaltura}")
print(f"Valor da hipotenusa: {trianguloretangulo1.hipotenusa}")


#QUESTÃO 4
class Ingresso:
  valor = 60

  def toString(self):
    valor_str = str(float(self.valor))
    return f"Valor do ingresso: R${valor_str}".title()

class IngressoVip(Ingresso):

  def toString(self):
    valor_adicional = 0.3 * super().valor
    valor_vip_str = str(float(super().valor + valor_adicional))
    return f"Valor do ingresso: R${valor_vip_str}".title()


print("\n---------------Questão 4---------------")
ing1 = Ingresso()
print(ing1.toString())
ing2 = IngressoVip()
print(ing2.toString())