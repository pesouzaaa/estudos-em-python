class Pessoas:
    def __init__(self, nome, ano_nascimento):
        self._nome =nome
        self.ano_nascimento = ano_nascimento


    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self.ano_nascimento
    

pessoa1 = Pessoas("Pedro", 2005)
print(f"Nome:{pessoa1.nome}\tIdade: {pessoa1.idade}")