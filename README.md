# Projeto Bank System

## Descrição
O **Projeto Bank System** é um sistema bancário desenvolvido em **Python** com foco em:
- Programação Orientada a Objetos (POO)
- Boas práticas de arquitetura
- Ferramentas modernas de desenvolvimento

O objetivo é simular operações bancárias básicas, como criação de contas, depósitos, saques e transferências, além de gerar relatórios e gráficos de movimentações financeiras.

---

## Funcionalidades
- Criação de contas (corrente e poupança)
- Operações bancárias:
  - Depósito
  - Saque
  - Transferência
- Relatórios e extratos:
  - Diário, semanal, mensal, anual
- Estrutura modular e escalável para futuras integrações (ex.: validação de CPF/CEP via API)

---

## Tecnologias utilizadas
- **Python 3.10+**
- **Poetry** → gerenciamento de dependências
- **Git + GitHub** → controle de versão
- **Linters e formatadores**:
  - `black` → formatação automática
  - `isort` → organização de imports
  - `flake8` → análise de estilo e erros
- **Testes**: `pytest`

### Futuro
- **SQLAlchemy** → ORM para persistência de dados
- **Pandas/Matplotlib** → relatórios e gráficos
- **APIs externas** → validação de CPF e CEP

---

## Estrutura do projeto
```bash
src/
└── banco/
    ├── models/
    │   ├── banco.py          # Classe abstrata Banco
    │   ├── banco_digital.py  # Classe concreta BancoDigital
    │   ├── banco_fisico.py   # Classe concreta BancoFisico
    │   ├── cliente.py        # Classe Cliente
    │   ├── endereco.py       # Classe Endereco
    │   ├── conta.py          # ContaCorrente, ContaPoupanca
    │   └── transacao.py      # Transações (depósito, saque, transferência)
└── services/
└── utils/
└── tests/

## Como executar
- **Clone o repositório:
git clone https://github.com/MarcelloAllves/Projeto_bank_system.git
cd Projeto_bank_system

## Instalação das dependências com Poetry:
poetry install

## Comando para execução dos testes:
poetry run pytest

## Exemplos de uso:
from banco.models.cliente import Cliente
from banco.models.conta import ContaCorrente

cliente = Cliente(nome="João Silva", cpf="12345678900")
conta = ContaCorrente(numero="0001", cliente=cliente)

conta.depositar(500)
conta.sacar(200)
print(conta.saldo)  # 300

## Atualizações Futuras:
Implementação de persistências untilizando a biblioteca SQLAlchemy
Gerar relatórios com utilizando as bibliotecas Pandas e Matplotlib
Testes de integração para validação entre os módulos, detectar falhas que testes unitários possam não detectar e pra tentar garantir que o fluxo de informações siga o esperado baseando-se em cenários reais de usabilidade dos usuários.

## Autor:
Marcelo Alves
" Estudante autônomo, em transição de carreira para desenvolvedor Python, em busca da primeira oportunidade | Portfólio em construção