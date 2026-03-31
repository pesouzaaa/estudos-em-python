from abc import ABC, abstractclassmethod
from datetime import datetime


class  Cliente:
    pass

class  PessoaFisica(Cliente):
    pass

class  Conta:
    PessoaFisica

class  ContaCorrente(Conta):
    pass

class  Historico:
    pass

class  Transacao(ABC):
    pass

class  Saque(Transacao):
    pass

class  Deposito(Transacao):
    pass
    
