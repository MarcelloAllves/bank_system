import pytest
from datetime import datetime, timezone

# Importe a classe real
from banco.models.cliente import Cliente

# Se você já tem Endereco em src/banco/models/endereco.py, importe-o:
# from banco.models.endereco import Endereco
# Caso ainda não tenha, use um stub mínimo para os testes:
class EnderecoStub:
    def __init__(self, rua: str, cidade: str):
        self.rua = rua
        self.cidade = cidade

    def __str__(self) -> str:
        return f"{self.rua}, {self.cidade}"


# -------- Fixtures (objetos de apoio) --------

@pytest.fixture
def endereco():
    # **Endereço padrão:** reutilizável em vários testes
    return EnderecoStub("Rua A", "Monte Carmelo")

@pytest.fixture
def cliente(endereco):
    # **Cliente padrão:** inicializado com dados válidos
    return Cliente(nome="Marcelo Silva", cpf="12345678900", endereco=endereco)


# -------- Testes de criação e validação --------

def test_cliente_cria_campos_basicos(endereco):
    c = Cliente(nome="Ana", cpf="11122233344", endereco=endereco)

    assert c.cliente_id == "CLI-11122233344"
    assert c.nome == "Ana"
    assert c.cpf == "11122233344"
    assert c.endereco == endereco
    # **Timestamps:** devem ser timezone-aware em UTC
    assert c.created_at.tzinfo is timezone.utc
    assert c.update_at.tzinfo is timezone.utc  # Nota: atributo no código é 'update_at'


@pytest.mark.parametrize("nome_invalido", ["", "   ", None])
def test_cliente_nome_invalido_levanta_erro(endereco, nome_invalido):
    with pytest.raises(ValueError) as exc:
        Cliente(nome=nome_invalido, cpf="123", endereco=endereco)
    assert "nome do cliente não pode ser vazio" in str(exc.value).lower()


@pytest.mark.parametrize("cpf_invalido", ["", "   ", None])
def test_cliente_cpf_invalido_levanta_erro(endereco, cpf_invalido):
    with pytest.raises(ValueError) as exc:
        Cliente(nome="João", cpf=cpf_invalido, endereco=endereco)
    assert "cpf do cliente não pode ser vazio" in str(exc.value).lower()


def test_cliente_ignora_cliente_id_parametro(endereco):
    # **Seu __init__ ignora cliente_id e gera a partir do CPF**
    c = Cliente(nome="Ana", cpf="99900011122", endereco=endereco, cliente_id="CLI-X")
    assert c.cliente_id == "CLI-99900011122"  # gerado pelo _generate_id


# -------- Testes de atualização de endereço --------

def test_atualizar_endereco_altera_objeto_e_timestamp(endereco, cliente, monkeypatch):
    novo = EnderecoStub("Rua B", "Uberlândia")

    # **Fixar o tempo** para tornar o teste determinístico
    fixed = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    monkeypatch.setattr(Cliente, "_now", staticmethod(lambda: fixed))

    cliente.atualizar_endereco(novo)

    assert cliente.endereco == novo
    assert cliente.update_at == fixed  # atualizado para o tempo fixo


# -------- Teste de serialização (to_dict) --------

def test_to_dict_retorna_dados_coerentes(endereco, monkeypatch):
    fixed_created = datetime(2025, 1, 1, 9, 0, 0, tzinfo=timezone.utc)
    fixed_updated = datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc)

    # **Patch sequencial:** primeiro criação, depois atualização
    call_times = [fixed_created, fixed_updated]
    monkeypatch.setattr(Cliente, "_now", staticmethod(lambda: call_times.pop(0)))

    c = Cliente(nome="Maria", cpf="55544433322", endereco=endereco)
    # Atualiza para forçar update_at diferente
    c.atualizar_endereco(EnderecoStub("Rua C", "Patrocínio"))

    d = c.to_dict()

    assert d["cliente_id"] == "CLI-55544433322"
    assert d["nome"] == "Maria"
    assert d["cpf"] == "55544433322"
    assert d["endereco"] == "Rua C, Patrocínio"  # usa __str__ do Endereco
    assert d["created_at"] == fixed_created.isoformat()
    assert d["update_at"] == fixed_updated.isoformat()


# -------- Teste de __str__ --------

def test_str_retorna_formato_legivel(endereco):
    c = Cliente(nome="Carlos", cpf="10101010101", endereco=endereco)
    s = str(c)
    assert "Cliente(" in s and "CPF=10101010101" in s and "Rua A, Monte Carmelo" in s


# pytest tests/test_cliente.py
