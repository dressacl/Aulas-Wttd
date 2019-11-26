class Meu_Objeto:
    def __init__(self):
        self.nome = str(input("Digite seu nome:"))
        self.idade = int(input("Digite sua idade:"))
        print('Construtor')
    def imprime(self):
        print('Olá, meu nome é %s e eu tenho %d anos'% (self.nome, self.idade))

pessoa = Meu_Objeto()
pessoa.imprime()
