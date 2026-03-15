class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe...")

    def latir(self):
        print("Auau")

def criar_cachorro():
    cao_2 = Cachorro("Tchuca", "Branco e perto")
    print("Criando o Cachorro:", cao_2.nome)

cao_1 = Cachorro("pop", "amarelo", False)
cao_1.latir()
criar_cachorro()

#forcar a destruicao - exemplo
print("Ola Mundo")

del cao_1 #usa a palavra resevada e ele destroi

print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")