class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Ave(Animal):
    def __init__(self,cor_bico, **kw):       
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): #**kw -> Kwargs
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):

        #print(Ornitorrinco.__mro__)# Mostra a ordem de resolucao

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

gato = Gato(nro_patas=4, cor_pelo="Preto")
print (gato)


# ! quando usado o **kw a declaracao de atributos devem estar como chave = valor
perry_ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo = "Verde", cor_bico = "Laranja" ) 
print(perry_ornitorrinco)