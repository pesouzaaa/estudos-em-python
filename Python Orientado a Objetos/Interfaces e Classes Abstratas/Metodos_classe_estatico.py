class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade 

    @classmethod #cria o metodo classe
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade) #ao inves de colocar return Pessoa - usa o cls

    @staticmethod # cria  o metodo estatico
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Pedro", 20)
# print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(2005, 7, 12, "Pedro") # Para chamar o método, nao precisa colocar "()" - basta chama-lo no ponto
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))