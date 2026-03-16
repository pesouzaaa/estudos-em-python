class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o Motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__ (self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.esta_carregado = carregado
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao'} Estou Carregado")
    

moto = motocicleta("Vermelha", "ABC1234", 2)
carro = carro("Preto", "DEF5678", 4)
caminhao = caminhao("Branco", "GHI9101", 8, True)

print(moto)
print(carro)
print(caminhao)