class Conta:
    def __init__(self, saldo):
        self._saldo=saldo #Ele e um recurso privado, ja que possui "_"

    #esses ja sao publicos, pois nao possui o "_"

    def __init__(self, depositar):    
        self.depositar=depositar
        
    def __init__(self, sacar):
        self.sacar= sacar

Contas = Conta(100)