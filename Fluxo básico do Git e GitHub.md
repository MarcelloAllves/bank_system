# 🚀 Fluxo Básico do Git e GitHub

## 1. Criar e iniciar o repositório
- `git init` → Cria um novo repositório Git na pasta atual.
- `git clone <url>` → Clona um repositório já existente do GitHub para sua máquina.

---

## 2. Configuração inicial
- `git config --global user.name "Seu Nome"` → Define seu nome para aparecer nos commits.
- `git config --global user.email "seu@email.com"` → Define seu e-mail para aparecer nos commits.

---

## 3. Verificar status
- `git status` → Mostra quais arquivos foram modificados e quais estão prontos para commit.

---

## 4. Adicionar arquivos ao *stage*
- `git add <arquivo>` → Adiciona um arquivo específico.
- `git add .` → Adiciona **todos os arquivos modificados**.

---

## 5. Criar o commit
- `git commit -m "mensagem clara"` → Cria um commit com os arquivos adicionados.
  - Exemplo: `git commit -m "feat: adiciona função de login"`

---

## 6. Conectar ao GitHub (se não foi clonado)
- `git remote add origin <url>` → Conecta seu repositório local ao remoto no GitHub.
- `git remote -v` → Lista