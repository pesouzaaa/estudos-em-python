class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    
    def buzinar (self):
        print("trim-trim")

    def parar (self):
        print("Parando bicicleta...")
        print("Bicileta Parada!")

    def correr (self):
        print("Comecando a pedalar")
        print("Vruuuum...")
        print("Bicicleta Correndo")
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike_01 = Bicicleta("Azul", "Caloi", 2024, 7000.00)
bike_01.correr()
bike_01.buzinar()
bike_01.parar()
print(bike_01)