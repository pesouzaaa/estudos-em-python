from abc import ABC, abstractclassmethod
from datetime import datetime


class  Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registar (conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class  PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class  Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo (self):
        return self._saldo
    
    @property
    def numero (self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
       saldo = self.saldo
       excedeu_saldo = valor > saldo

       if excedeu_saldo:
           print("\n@@@ Operacao falhou! Voce nao tem saldo suficiente. @@@")
       
       elif valor > 0:
           self._saldo -= valor
           print("\n### Saque realizado com sucesso! ###")
           return True

       else: 
           print("\n@@@ A operacao falhou! O valor informado é invalido. @@@") 
       
       return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n#### Deposito realizado om sucesso! ###")
        else:
            print("\n@@@ Operacao falhou! O valor informado é inválido. @@@")
            return False
        
        return True

class  ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            (transacao for transacao in self.historico.transacoes if transacao ["tipo"]== Saque.__name__)
        )
#06:02

class  Historico:
    pass

class  Transacao(ABC):
    pass

class  Saque(Transacao):
    pass

class  Deposito(Transacao):
    pass
    
