from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime, timezone
import random
from typing import Dict, Optional, Any

from banco.models.cliente import Cliente
from banco.models.conta import Conta
from banco.models.transacao import Transacao


class Banco(ABC):
    """
    Classe abstrata que define os contratos fundamentais para um sistema bancário.

    Subclasses concretas (ex.: BancoDigital, BancoFisico) devem implementar os métodos
    obrigatórios, garantindo consistência nas operações de clientes, contas e transações.

    Atributos:
        nome (str): Nome do banco.
        clientes (Dict[str, Cliente]): Cache local de clientes.
        contas (Dict[str, Conta]): Cache local de contas.
        cliente_repo (Any, opcional): Repositório injetável para persistência de clientes.
        conta_repo (Any, opcional): Repositório injetável para persistência de contas.
    """

    def __init__(
        self,
        nome: str,
        cliente_repo: Optional[Any] = None,
        conta_repo: Optional[Any] = None,
    ) -> None:
        self.nome = nome
        self.clientes: Dict[str, Cliente] = {}
        self.contas: Dict[str, Conta] = {}
        self.cliente_repo = cliente_repo
        self.conta_repo = conta_repo

    @staticmethod
    def _generate_id() -> int:
        """
        Gera um identificador de conta aleatório entre 4 e 6 dígitos.

        Returns:
            int: Identificador numérico da conta.
        """
        return random.randint(1000, 999999)

    @staticmethod
    def _now() -> datetime:
        """
        Retorna o timestamp atual em UTC.

        Usado para preencher atributos de auditoria:
            - created_at: data/hora da criação do objeto (definido uma única vez).
            - updated_at: data/hora da última modificação do objeto (atualizado sempre que há mudanças).

        Returns:
            datetime: Data e hora atual em UTC.
        """
        return datetime.now(timezone.utc)


    @abstractmethod
    def cadastrar_cliente(self, cliente_dto: Dict[str, Any]) -> str:
        """
        Cadastra um novo cliente.

        Args:
            cliente_dto (Dict[str, Any]): Dados do cliente (nome, cpf, endereço, etc.).

        Returns:
            str: Identificador único do cliente.

        Raises:
            ValueError: Se dados obrigatórios estiverem ausentes.
            ClienteJaExiste: Se CPF já estiver cadastrado.
        """
        raise NotImplementedError

    @abstractmethod
    def abrir_conta(
        self, cliente_id: str, tipo_conta: str, saldo_inicial: float = 0.0
    ) -> str:
        """
        Abre uma conta vinculada a um cliente existente.

        Args:
            cliente_id (str): Identificador do cliente.
            tipo_conta (str): Tipo da conta ('corrente', 'poupanca', ...).
            saldo_inicial (float, opcional): Saldo inicial da conta. Default = 0.0.

        Returns:
            str: Identificador único da conta.

        Raises:
            ClienteNaoEncontrado: Se o cliente não existir.
            ValueError: Se o saldo inicial for negativo.
        """
        raise NotImplementedError

    @abstractmethod
    def realizar_transacao(
        self,
        origem_id: Optional[str],
        destino_id: Optional[str],
        valor: float,
        tipo: str,
    ) -> str:
        """
        Executa uma transação bancária (depósito, saque ou transferência).

        Args:
            origem_id (Optional[str]): Conta de origem (None em depósitos).
            destino_id (Optional[str]): Conta de destino (None em saques).
            valor (float): Valor da transação (> 0).
            tipo (str): Tipo da transação ('deposito', 'saque', 'transferencia').

        Returns:
            str: Código de confirmação ou mensagem de sucesso.

        Raises:
            ContaNaoEncontrada: Se conta(s) não existir(em).
            SaldoInsuficiente: Se saldo da origem for insuficiente.
            ValueError: Se valor <= 0.
        """
        raise NotImplementedError

    @abstractmethod
    def gerar_relatorio(self, tipo: str = "resumo") -> Dict[str, Any]:
        """
        Gera relatórios sobre clientes, contas e transações.

        Args:
            tipo (str, opcional): Tipo de relatório. Default = "resumo".
                Possíveis valores: "resumo", "detalhado", "financeiro", "clientes".

        Returns:
            Dict[str, Any]: Estrutura de dados com informações do relatório.
        """
        raise NotImplementedError
