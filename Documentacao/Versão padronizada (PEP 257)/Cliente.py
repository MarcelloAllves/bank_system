from __future__ import annotations
from datetime import datetime, timezone
from typing import Optional, Dict, Any
from banco.models.endereco import Endereco


class Cliente:
    """
    Representa um cliente do banco, armazenando informações pessoais,
    endereço e metadados de criação/atualização.

    Atributos:
        cliente_id (str): Identificador único do cliente (CLI-<cpf>).
        nome (str): Nome completo do cliente.
        cpf (str): CPF do cliente (único e obrigatório).
        endereco (Endereco): Endereço associado ao cliente.
        created_at (datetime): Data/hora de criação em UTC.
        updated_at (datetime): Última atualização em UTC.
    """

    def __init__(self, nome: str, cpf: str, endereco: Endereco, cliente_id: Optional[str] = None) -> None:
        """
        Construtor da classe Cliente.

        Args:
            nome (str): Nome completo do cliente.
            cpf (str): CPF do cliente.
            endereco (Endereco): Endereço associado ao cliente.
            cliente_id (Optional[str]): Identificador único. Se não informado, será gerado automaticamente.

        Raises:
            ValueError: Se nome ou CPF forem vazios.
        """
        if not nome or not nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio!")
        if not cpf or not cpf.strip():
            raise ValueError("O campo CPF do cliente não pode ser vazio!")

        self.cliente_id = cliente_id or self._generate_id(cpf)
        self.nome = nome.strip()
        self.cpf = cpf.strip()
        self.endereco = endereco
        self.created_at = self._now()
        self.updated_at = self.created_at

    @staticmethod
    def _generate_id(cpf: str) -> str:
        """
        Gera um identificador único para o cliente baseado no CPF.

        Args:
            cpf (str): CPF do cliente.

        Returns:
            str: Identificador no formato CLI-<cpf>.
        """
        return f"CLI-{cpf}"

    @staticmethod
    def _now() -> datetime:
        """
        Retorna o timestamp atual em UTC.

        Usado para preencher atributos de auditoria:
            - created_at: data/hora da criação do objeto.
            - updated_at: data/hora da última modificação.

        Returns:
            datetime: Data e hora atual em UTC.
        """
        return datetime.now(timezone.utc)

    def atualizar_endereco(self, novo_endereco: Endereco) -> None:
        """
        Atualiza o endereço do cliente e o campo updated_at.

        Args:
            novo_endereco (Endereco): Novo endereço do cliente.
        """
        self.endereco = novo_endereco
        self.updated_at = self._now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte os dados do cliente em um dicionário (DTO).

        Returns:
            Dict[str, Any]: Representação do cliente em formato dicionário.
        """
        return {
            "cliente_id": self.cliente_id,
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": str(self.endereco),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __str__(self) -> str:
        """
        Retorna uma representação legível do cliente.

        Returns:
            str: Representação textual do cliente.
        """
        return f"Cliente({self.nome}, CPF={self.cpf}, Endereço={self.endereco})"
