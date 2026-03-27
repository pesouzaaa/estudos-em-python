from abc import ABC, abstractmethod #Ele está importando um módulo [Pique importar uma biblioteca]  

class ControleRemoto (ABC):
    @abstractmethod #quando o método estiver declarado como abstrato -->
    def ligar (self):
        pass

    @abstractmethod
    def desligar (self):
        pass    

    @property # Primeiro Fala que é propriedade
    @abstractmethod #Depois que é abstrata - No metodo antigo era declarado com @abstractproperty
    def marca(self):
        pass


class ControleTV (ControleRemoto): # --> É preciso que eu implemente novamente, pois nao instancia
    def ligar(self):
        print("Ligando...")

    def desligar(self):
        print("Desligando...")    

    @property
    def marca (self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)