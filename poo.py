from math import sqrt

'''EXERCÍCIOS BÁSICOS SOBRE CONCEITOS DE POO

1. Crie uma classe “Produto” que possua os atributos “nomeloja” e “preco”, crie os métodos sets e gets para estes atributos. 
Crie também o atributo “descrição” e seu método chamado “getDescrição” que retorna uma 
string com o simples conteúdo “Produto de informática”. '''

'''primeira questao'''

"""class Produto:
    descricao = " Produto de  Informática"

    def __init__(self, nomeloja, preco):
        self._nomeloja = nomeloja
        self._preco = preco
       
    @classmethod
    def getdescricao(cls):
        return cls.descricao

    @property
    def nomeloja(self):
        return self._nomeloja 

    @nomeloja.setter
    def nomeloja(self,nome):
        self._nomeloja = nome

    @property
    def preco(self):
        return self._preco 

    @nomeloja.setter
    def nomeloja(self,valor):
        self._preco += valor
   
    
p1 = Produto ("lelevariedades", 56)
print(f"nome da loja: {p1.nomeloja}")
print(f"preço: {p1.preco}")
print(p1.getdescricao())
"""
'''questão dois 
2. Crie uma classe chamada Retângulo. Esta classe tem como atributos encapsulados altura e largura (ou seja,
estas propriedades não serão visíveis pelo objeto). Crie dois métodos da seguinte forma: o primeiro para pedir e
atribuir valor para altura e o segundo para pedir e atribuir valor para largura.
'''
"""class Retangulo:
    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura

    def alteraaltura(self):
        altura = float(input("informe altura  "))
        self._altura = altura

    def alteralargura(self):
        largura = float(input("informe largura  "))
        self._largura = largura

r1 = Retangulo(25, 15)
print(f"altura: {r1._altura}")
print(f"altura: {r1._largura}")
r1.alteraaltura()
r1.alteralargura()
print(f"altura: {r1._altura}")
print(f"altura: {r1._largura}")

"""
"""3. Crie uma classe chamada trianguloretangulo. Esta classe tem como atributos encapsulados
 a catetobase e a catetoaltura. Crie dois métodos 
para pedir e atribuir valores separadamente para base e altura. Crie mais um atributo encapsulado
 chamado hipotenusa. Este atributo não será informado pelo usuário. Ele será calculado através de um 
 método que utiliza os valores dos catetos lidos anteriormente e determinados através da fórmula a^2 = b^2 
 +c^2. Crie o método e calcule a hipotenusa."""

"""class Trianguloretangulo:
    def _init_(self):
        self.catetobase = 0
        self.catetoaltura = 0
        self.hipotenusa = 0

    def recebe_altura(self):
        catetoaltura = float(input("informe a altura"))
        self.catetoaltura = catetoaltura

    def recebe_base(self):
        catetobase = float(input("informe a base"))
        self.catetobase = catetobase

    def calculo_hipotenusa(self):
        self.hipotenusa = sqrt( self.catetobase**2 + self.catetoaltura**2)

t1 = Trianguloretangulo()
t1.recebe_base()
t1.recebe_altura()
t1.calculo_hipotenusa()
print(f"cateto altura:{t1.catetoaltura}")
print(f"cateto base:{t1.catetobase}")
print(f"hipotenusa : {t1.hipotenusa}")"""

"""4. Crie uma classe chamada Ingresso que possua um atributo valor e um método toString que retorne à informação do valor do ingresso.
a. Crie uma classe IngressoVIP, que herda de Ingresso e possui um atributo valor
Adicional. O método toString da classe IngressoVIP deve considerar que o valor do
ingresso é o valor da superclasse somado ao valor Adicional do IngressoVIP.
b. Crie uma classe para testar os objetos das classes Ingresso e IngressoVIP.
"""

class ingresso:
    valor = 10

    def tostring(self):
        valor_str = str(self.valor)
        print(f"valor do ingresso: {valor_str}")

class IngressoVIP(ingresso):
    valor_adicional = 0
    valor_total = 0

    def tostring(self):
        valor_adicional = 6
        valor_total = float(valor_adicional + super().valor)
        valor_total = str(valor_total)
        print(f"valor do ingresso com adicional: {valor_total}")

ig1 = ingresso()
print(ig1.tostring())
ig2 = IngressoVIP()
print(ig2.tostring())



    
    
        