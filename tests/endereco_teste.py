from banco.models.endereco import Endereco

endereco = Endereco(
    rua="Av. Brasil",
    numero="123",
    bairro="Centro",
    cidade="Monte Carmelo",
    estado="MG",
    cep="38500-000",
    complemento="Casa"
)
print(endereco)