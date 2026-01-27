from excecoes import (
    SaldoInsuficienteError,
    LimiteExcedidoError,
    LimiteSaquesError,
    ValorInvalidoError,
)

class Conta:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self,valor):
        if valor <=0:
            raise ValorInvalidoError("Valor inválido para depósito.")
        
        self.saldo += valor
        self.extrato += f"Depósito: R$ {valor:.2f}\n"

    def sacar(self, valor):
        if valor <=0:
            raise ValorInvalidoError("Valor inválido para saque.")
        
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        
        if valor > self.limite: 
            raise LimiteExcedidoError("Valor excede o limite permitido.")
        
        if self.numero_saques >=self.LIMITE_SAQUES:
            raise LimiteSaquesError("Número máximo de saques excedido.")
        
        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques +=1

    def mostrar_extrato(self):
        print("\n============ EXTRATO ============")
        print("Não foram realizado movimentações." if not self.extrato else self.extrato)
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("====================================")