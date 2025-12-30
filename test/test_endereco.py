import pytest
from banco.models.endereco import Endereco


# -------- Testes de criação válida --------


def test_endereco_criado_com_campos_validos():
    e = Endereco(
        rua="Rua das Flores",
        numero="123",
        bairro="Centro",
        cidade="Monte Carmelo",
        estado="MG",
        cep="38500-000",
        complemento="Apto 45",
    )

    assert e.rua == "Rua das Flores"
    assert e.numero == "123"
    assert e.bairro == "Centro"
    assert e.cidade == "Monte Carmelo"
    assert e.estado == "MG"
    assert e.cep == "38500-000"
    assert e.complemento == "Apto 45"


def test_endereco_remove_espacos_em_campos():
    e = Endereco(
        rua="  Rua Teste  ",
        numero="  10 ",
        bairro=" Bairro ",
        cidade=" Cidade ",
        estado=" SP ",
        cep=" 00000-000 ",
    )
    assert e.rua == "Rua Teste"
    assert e.numero == "10"
    assert e.bairro == "Bairro"
    assert e.cidade == "Cidade"
    assert e.estado == "SP"
    assert e.cep == "00000-000"
    assert e.complemento == ""


# -------- Testes de validação --------


@pytest.mark.parametrize(
    "campo,valor",
    [
        ("rua", ""),
        ("numero", "   "),
        ("bairro", None),
        ("cidade", ""),
        ("estado", " "),
        ("cep", None),
    ],
)
def test_endereco_campos_obrigatorios_invalidos_levantam_erro(campo, valor):
    kwargs = {
        "rua": "Rua A",
        "numero": "1",
        "bairro": "Centro",
        "cidade": "Cidade",
        "estado": "MG",
        "cep": "12345-678",
    }
    kwargs[campo] = valor
    with pytest.raises(ValueError) as exc:
        Endereco(**kwargs)
    assert f"campo {campo}" in str(exc.value).lower()


# -------- Teste de __str__ --------


def test_str_retorna_formato_legivel():
    e = Endereco(
        rua="Av. Brasil",
        numero="500",
        bairro="Industrial",
        cidade="Uberlândia",
        estado="MG",
        cep="38400-000",
        complemento="Bloco B",
    )
    s = str(e)
    assert "Av. Brasil, 500 - Industrial, Uberlândia/MG, CEP: 38400-000 (Bloco B)" == s


def test_str_sem_complemento():
    e = Endereco(
        rua="Av. Goiás",
        numero="10",
        bairro="Centro",
        cidade="Goiânia",
        estado="GO",
        cep="74000-000",
    )
    s = str(e)
    assert "Av. Goiás, 10 - Centro, Goiânia/GO, CEP: 74000-000" == s


# pytest tests/test_endereco.py
