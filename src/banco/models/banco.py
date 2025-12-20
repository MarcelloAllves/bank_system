from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime, timezone
import random
from typing import Dict, Optional, Any


from banco.models.cliente import Cliente
from banco.models.conta import Conta
from banco.models.transacao import Transacao

nome: str
clientes: Dict[str, Cliente]
contas: Dict[str, Conta]


class Banco(ABC):
    def __init__(
        self,
        nome: str,
        cliente_repo: Optional[Any] = None,
        conta_repo: Optional[Any] = None,
    ) -> None:
        self.nome = nome
        # coleções locais (cache) opcionais; preferir usar repositórios injetados
        self.clientes = {}
        self.contas = {}

        # repositórios injetáveis (interfaces simples esperadas: add/get/remove/list)
        self.cliente_repo = cliente_repo
        self.conta_repo = conta_repo

    @staticmethod
    def _generate_id() -> int:
        """Gera um id_conta entre 4 e 6 dígitos."""
        return random.randint(1000, 999999)

    @staticmethod
    def _now() -> datetime:
        """Os atributos created_at e updated_at devem guardar timestamps em UTC,
        e não em horário local. Isso evita problemas de fuso horário quando o
        sistema é usado em diferentes regiões do mundo."""
        return datetime.now(timezone.utc)

    @abstractmethod
    def cadastrar_cliente(self, cliente_dto: dict) -> str:
        """
        Cadastra um cliente e retorna o cliente_id.
        Toda classe que herdar da classe abstrata deve implementar o método
        cadastrar_cliente.
        O método recebe um dicionário com dados do cliente e deve retornar uma
        string.
        Se não for implementado, o Python lança NotImplementedError.

        Args:
            cliente_dto: espera receber um dicionário com os dados do cliente (DTO = Data Transfer Object).
            dicionário com dados necessários (nome, cpf, endereco, ...)

        Raises:
            Essa linha lança uma exceção sempre que o método for chamado sem ter
                sido implementado.
            É uma forma de reforçar que esse método não deve ser usado
                diretamente na classe abstrata.
            Quando uma subclasse sobrescreve esse método, ela substitui essa
                exceção por uma implementação real.
            ValueError: se dados obrigatórios estiverem ausentes.
            ClienteJaExiste: se CPF já cadastrado (defina em banco.exceptions).
        """
        raise NotImplementedError

    @abstractmethod
    def abrir_conta(
        self, cliente_id: str, tipo_conta: str, saldo_inicial: float = 0.0
    ) -> str:
        """
        Abre uma conta para o cliente identificado por cliente_id e retorna conta_id.
        Em resumo:
            Esse método define a assinatura de como abrir uma conta deve funcionar, mas não implementa a lógica.
            Ou seja, ele diz:
                Toda classe que herdar de Banco precisa ter um método abrir_conta que receba cliente_id, tipo_conta
                e saldo_inicial, e retorne uma string.
                Mas deixa para a subclasse decidir como isso será feito.
        Args:
            cliente_id: id do cliente já cadastrado.
            tipo_conta: 'corrente' | 'poupanca' | ...
            saldo_inicial: saldo inicial (>= 0) saldo inicial da conta. Se não for informado, assume 0.0 por padrão.

        Raises:
            ClienteNaoEncontrado: se cliente_id não existir.
            ValueError: se saldo_inicial for negativo.
            Essa linha lança uma exceção sempre que o método for chamado sem ter
            sido implementado.
            É usado em classes abstratas para indicar que esse método é apenas
            um contrato:
                Ele deve ser sobrescrito por qualquer subclasse concreta.
                Se não for sobrescrito, chamar esse método vai gerar erro.
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
        Em resumo
            Esse método define a interface para transações bancárias:
            Ele descreve os parâmetros necessários (origem, destino, valor, tipo).
            Ele exige que subclasses implementem a lógica (como atualizar saldos, registrar transações,
                validar limites).
            Ele retorna uma string como resultado da operação.

        - tipo: str → tipo da transação (ex.: "deposito", "saque", "transferencia").
        - origem_id: Optional[str] → identificador da conta de origem. Pode ser None (por exemplo, em depósitos).
        - destino_id: Optional[str] → identificador da conta de destino. Também pode ser None (por exemplo, em saques).
        - Para deposito: origem_id=None, destino_id=conta_id
        - Para saque: origem_id=conta_id, destino_id=None
        - Para transferencia: origem_id=conta_origem_id, destino_id=conta_destino_id
        - -> str → o método deve retornar uma string (por exemplo, um código de confirmação ou mensagem de sucesso).

        Raises:
            ContaNaoEncontrada: se conta(s) não existir(em).
            SaldoInsuficiente: se origem não tiver saldo suficiente.
            ValueError: se valor <= 0.
            Lança uma exceção se o método for chamado sem implementação.
            Isso reforça que o método não deve ser usado diretamente na classe abstrata.
            A subclasse precisa sobrescrever esse método com a lógica real.
        """
        raise NotImplementedError

    @abstractmethod
    def gerar_relatorio(self, tipo: str = "resumo") -> dict:
        """
        Em resumo:
            Esse método define a interface para geração de relatórios:
            Ele descreve os parâmetros necessários (tipo de relatório).
            Ele exige que subclasses implementem a lógica (como coletar dados de clientes, contas, transações).
            Ele retorna um dicionário com os resultados.

        tipo: str = "resumo" → parâmetro opcional que define o tipo de relatório.
            Se não for informado, assume "resumo" como padrão.
            Poderia haver outros tipos, como "detalhado", "financeiro", "clientes", etc.
        -> dict → indica que o método deve retornar um dicionário (estrutura chave-valor),
        com os dados do relatório.

        - Não gera arquivos; retorna estruturas (dict/list) que um gerador de relatório
          (service ou util) transforma em CSV/Excel/Gráfico.

        raise NotImplementedError:
            Lança uma exceção se o método for chamado sem implementação.
            Isso reforça que o método não deve ser usado diretamente na classe abstrata.
            A subclasse precisa sobrescrever esse método com a lógica real de geração de relatórios.
        """
        raise NotImplementedError
