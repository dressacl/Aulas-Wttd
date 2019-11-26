"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""
class Quadrado():
    def __init__(self):
        self.tam_lado = 1

    def Muda_valor_lado(self, tam_lado):
        tam_lado = 5

    def Retorna_valor_lado(self):
        return self.tam_lado
        print(self.tam_lado)

    def area(self):
        return self.tam_lado**2