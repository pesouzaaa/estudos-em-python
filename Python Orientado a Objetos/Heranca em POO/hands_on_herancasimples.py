class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o Motor...")


class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def esta_carregado(self):
        print("Nao Estou Carregado")
    

moto = motocicleta("Vermelha", "ABC1234", 2)
moto.ligar_motor()

carro = carro("Preto", "DEF5678", 4)
carro.ligar_motor()

caminhao = caminhao("Branco", "GHI9101", 8)
caminhao.ligar_motor()
caminhao.esta_carregado()
