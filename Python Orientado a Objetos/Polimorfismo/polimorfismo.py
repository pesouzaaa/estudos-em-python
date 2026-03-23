class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao voa")

def plano_de_voo(obj): #aqui esta o polimorfismo
    obj.voar()         #a mesma chamada se comporta diferente dependendo do objeto

plano_de_voo(Pardal())
plano_de_voo(Avestruz())