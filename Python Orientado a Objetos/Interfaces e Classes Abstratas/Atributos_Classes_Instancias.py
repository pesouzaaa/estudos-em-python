class Estudante:
    escola = "DevLune" #Atributo de Classe

    def __init__(self, nome, numero): #Atributo de Instancia
        self.nome = nome 
        self.numero = numero

    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
pe = Estudante("Pedro", 609843)
babi = Estudante("Barbara", 8209383)
mostrar_valores(pe, babi)

Estudante.escola = "NewSchool"
thico = Estudante("Thiago", 9023309)
mostrar_valores(pe, babi, thico)
