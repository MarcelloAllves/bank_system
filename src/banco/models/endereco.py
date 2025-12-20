class Endereco:
    """
    Representa um endereço físico de um cliente ou entidade.

    Esta classe garante que todos os campos obrigatórios sejam preenchidos
    corretamente (não nulos e não apenas espaços em branco).
    É utilizada para armazenar e manipular informações de localização.

    Atributos:
        rua (str): Nome da rua ou logradouro.
        numero (str): Número do imóvel.
        bairro (str): Bairro onde o imóvel está localizado.
        cidade (str): Cidade do endereço.
        estado (str): Estado (UF) do endereço.
        cep (str): Código de Endereçamento Postal (CEP).
        complemento (str, opcional): Informação adicional, como apartamento ou bloco.

    Métodos:
        __init__(...):
            Inicializa um objeto Endereco validando os campos obrigatórios.
        __str__():
            Retorna o endereço formatado como string legível.
    """

    def __init__(
        self,
        rua: str,
        numero: str,
        bairro: str,
        cidade: str,
        estado: str,
        cep: str,
        complemento: str,
    ) -> None:
        # Criando validação para que campos necessários não sejam preenchidos
        # com valor nulo ou somente com espaços.
        for campo, valor in {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": str,
            "cep": str,
        }.items():
            if not valor or valor.strip():
                raise ValueError(f"O campo '{campo}' não pode ser vazio!")
        self.rua = rua.strip()
        self.numero = numero.strip()
        self.bairro = bairro.strip()
        self.cidade = cidade.strip()
        self.estado = estado.strip()
        self.cep = cep.strip()
        self.complemento = complemento.strip()
