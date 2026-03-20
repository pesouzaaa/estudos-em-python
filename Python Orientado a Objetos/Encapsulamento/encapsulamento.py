class Conta:
    def __init__(self, saldo, nro_agencia):
        self._saldo=saldo #Ele e um recurso privado, ja que possui "_"
        self.nro_agencia = nro_agencia #Ja este e um recurso publico, pois nao possui "_"


    def depositar(self, valor):    
        self._saldo += valor
        
    def sacar(self, valor):
        self._saldo -= valor
        

conta = Conta(100, "0001")
conta.depositar(100)
print(conta.nro_agencia)