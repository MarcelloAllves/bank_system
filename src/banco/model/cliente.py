# src/banco/models/cliente.py

from __future__ import annotations
from datetime import datetime, timezone
from typing import Optional
from banco.model.endereco import Endereco


class Cliente:
    """
    Representa um cliente do banco.

    Imports e anotações de tipo:

        from __future__ import annotations: Habilita anotações de tipo atrasadas,
            permitindo referenciar tipos (como Endereco) como strings ou sem
            avaliação imediata, útil para evitar importações circulares.

        from datetime import datetime, timezone: Importa datetime e timezone para
            trabalhar com timestamps e garantir que sejam em UTC.

        from typing import Optional: Fornece o tipo Optional[...] para indicar
            que um parâmetro pode ser do tipo especificado ou None.

        from banco.models.endereco import Endereco:  Importa a classe Endereco
            usada como tipo para o atributo de endereço do cliente.

    Atributos:
        cliente_id (str): Identificador único do cliente.
        nome (str): Nome completo do cliente.
        cpf (str): CPF do cliente (único).
        endereco (Endereco): Endereço associado ao cliente.
        created_at (datetime): Data/hora de criação em UTC.
        updated_at (datetime): Última atualização em UTC.

    Métodos estáticos auxiliares:

        @staticmethod:
            - Indica que o método não usa self nem cls;
            - é utilitário ligado à classe.

        def _generate_id(cpf: str) -> str:
            -Método que gera um identificador baseado no CPF.

        return f"CLI-{cpf}:
            - Retorna uma string no formato CLI-<cpf>, simples e previsível.

        def _now() -> datetime:
            - Método que retorna o timestamp atual em UTC.

        return datetime.now(timezone.utc):
            - Usa timezone.utc para garantir que o tempo seja timezone-aware
                em UTC.

    Métodos:
        atualizar_endereco(novo_endereco): Atualiza o endereço do cliente.
        to_dict(): Converte os dados do cliente em formato dicionário.
        __str__(): Retorna uma representação legível do cliente.
    """

    def __init__(
        self,
        nome: str,
        cpf: str,
        endereco: Endereco,
        cliente_id: Optional[str] = None,
    ) -> None:
        if not nome or not nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio!")
        if not cpf or not cpf.strip():
            raise ValueError("O campo CPF do cliente não pode ser vazio!")
        if not cpf.isdigit() or len(cpf) != 11: 
            raise ValueError("CPF deve conter 11 dígitos numéricos.")

        self.cliente_id = self._generate_id(cpf)
        self.nome = nome.strip()
        self.cpf = cpf.strip()
        self.endereco = endereco
        self.created_at = self._now()
        self.updated_at = self.created_at

    @staticmethod
    def _generate_id(cpf: str) -> str:
        """Irá gerar um identificador único para o cliente basedo no cpf."""
        return f"CLI-{cpf}"

    @staticmethod
    def _now() -> datetime:
        """Retorna timestamp UTC."""
        return datetime.now(timezone.utc)

    def atualizar_endereco(self, novo_endereco: Endereco) -> None:
        """Irá atualizar o endereço do cliente e registrar o timestamp."""
        self.endereco = novo_endereco
        self.updated_at = self._now()

    def to_dict(self) -> dict:
        """Edição da representação em dicionário (DTO)."""
        return {
            "cliente_id": self.cliente_id,
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": str(self.endereco),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __str__(self) -> str:
        return f"Cliente({self.nome}, CPF={self.cpf}, Endereço={self.endereco})"
