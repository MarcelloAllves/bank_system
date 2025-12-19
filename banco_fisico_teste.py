from .banco import Banco

class BancoFisico(Banco):
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado no banco físico {self.nome}")

    def abrir_conta(self, cliente, tipo_conta: str):
        conta = {"cliente": cliente, "tipo": tipo_conta, "saldo": 0}
        self.contas.append(conta)
        print(f"Conta {tipo_conta} aberta para {cliente.nome} no banco físico {self.nome}")
        return conta

    def realizar_transacao(self, conta, valor: float, tipo: str):
        if tipo == "deposito":
            conta["saldo"] += valor
        elif tipo == "saque":
            conta["saldo"] -= valor
        print(f"Transação {tipo} de {valor} realizada na conta de {conta['cliente'].nome}")

    def gerar_relatorio(self):
        print(f"Banco Físico {self.nome} possui {len(self.clientes)} clientes e {len(self.contas)} contas.")
