from abc import ABC, abstractmethod

class Banco(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.clientes = []
        self.contas = []

    @abstractmethod
    def cadastrar_cliente(self, cliente):
        """Método abstrato para cadastrar um cliente"""
        pass

    @abstractmethod
    def abrir_conta(self, cliente, tipo_conta: str):
        """Método abstrato para abrir uma conta"""
        pass

    @abstractmethod
    def realizar_transacao(self, conta, valor: float, tipo: str):
        """Método abstrato para saque, depósito ou transferência"""
        pass

    @abstractmethod
    def gerar_relatorio(self):
        """Método abstrato para gerar relatórios do banco"""
        pass

        """_summary_
            O que está acontecendo aqui
            Banco herda de ABC → significa que é uma classe abstrata.

            Métodos com @abstractmethod → obrigam qualquer classe filha a implementar.

            Atributos básicos (nome, clientes, contas) → já dão estrutura inicial.
        """