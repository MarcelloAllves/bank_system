class Endereco:
    """
    Representa um endereço físico de um cliente ou entidade.

    Atributos:
        rua (str): Nome da rua ou logradouro.
        numero (str): Número do imóvel.
        bairro (str): Bairro onde o imóvel está localizado.
        cidade (str): Cidade do endereço.
        estado (str): Estado (UF).
        cep (str): Código de Endereçamento Postal.
        complemento (str, opcional): Informação adicional, como apartamento ou bloco.

    Exceções:
        ValueError: Lançada se algum campo obrigatório for vazio ou apenas espaços.

    Exemplo:
        >>> endereco = Endereco(
        ...     rua="Rua das Flores",
        ...     numero="123",
        ...     bairro="Centro",
        ...     cidade="Belo Horizonte",
        ...     estado="MG",
        ...     cep="30123-456",
        ...     complemento="Apto 45"
        ... )
        >>> print(endereco)
        Rua das Flores, 123 - Centro, Belo Horizonte/MG, CEP: 30123-456 (Apto 45)
    """

    def __init__(
        self,
        rua: str,
        numero: str,
        bairro: str,
        cidade: str,
        estado: str,
        cep: str,
        complemento: str = "",
    ) -> None:
        """
        Inicializa um objeto Endereco validando os campos obrigatórios.

        Args:
            rua (str): Nome da rua ou logradouro.
            numero (str): Número do imóvel.
            bairro (str): Bairro onde o imóvel está localizado.
            cidade (str): Cidade do endereço.
            estado (str): Estado (UF).
            cep (str): Código de Endereçamento Postal.
            complemento (str, opcional): Informação adicional, como apartamento ou bloco.

        Raises:
            ValueError: Se algum campo obrigatório for vazio ou apenas espaços.
        """
        for campo, valor in {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep,
        }.items():
            if not valor or not valor.strip():
                raise ValueError(f"O campo {campo} não pode ser vazio!")
        self.rua = rua.strip()
        self.numero = numero.strip()
        self.bairro = bairro.strip()
        self.cidade = cidade.strip()
        self.estado = estado.strip()
        self.cep = cep.strip()
        self.complemento = complemento.strip() if complemento else ""

    def __str__(self) -> str:
        """
        Retorna o endereço formatado como string legível.

        Returns:
            str: Endereço completo no formato:
                 "Rua, Número - Bairro, Cidade/Estado, CEP: XXXXX-XXX (Complemento)"
        """
        endereco = f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}, CEP: {self.cep}"
        if self.complemento:
            endereco += f" ({self.complemento})"
        return endereco
