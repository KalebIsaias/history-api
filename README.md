# History API

## Introdução

Esta documentação descreve como instalar as dependências e rodar a API, além de detalhar todos os endpoints e seus parâmetros.

## Instalação

### Passo 1: Clonar o repositório

Clone o repositório do projeto em sua máquina local.

```bash
git clone https://github.com/KalebIsaias/history-api.git
cd history-api
```

### Passo 2: Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate      # Windows
```

### Passo 3: Instale as dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configure as variáveis de ambiente

Crie um arquivo .env na raiz do repositório e cole:

```
DEBUG=False
TITLE=History API
ORIGINS=
SECRET_KEY=test
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
SQLITE_CONNECTION_STRING=sqlite:///database.db
POSTGRES_HOST=history-db.ceynz4t1zagz.us-east-1.rds.amazonaws.com
POSTGRES_PORT=5432
POSTGRES_DB=history_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=12345678
GOOGLE_API_KEY=AIzaSyBtOGD2imhSbkPWePDh4DZRWhhYBANsJ20
```

### Passo 5: Inicie o servidor

```
uvicorn main:app --reload
```

A API estará disponível em http://localhost:8000

---

# Documentação das Rotas

## Endpoints da História (/history)

### Listar todas as histórias

- **Método HTTP:** GET
- **URL:** `/history/`
- **Descrição:** Retorna todas as histórias.
- **Parâmetros:** Nenhum
- **Retorno:** Lista de todas as histórias cadastradas.

### Obter uma história pelo ID

- **Método HTTP:** GET
- **URL:** `/history/{history_id}`
- **Descrição:** Retorna uma história pelo ID especificado.
- **Parâmetros:** 
  - `history_id` (int): ID da história a ser obtida.
- **Retorno:** Detalhes da história com o ID especificado.

### Criar uma nova história

- **Método HTTP:** POST
- **URL:** `/history/`
- **Descrição:** Cria uma nova história com os dados fornecidos.
- **Parâmetros JSON:** 
  - `title` (str): Título da história.
  - `description` (str): Descrição da história.
  - `category` (str): Categoria da história.
  - `content` (str): Conteúdo da história.
- **Retorno:** Detalhes da história recém-criada.

### Aprimorar uma história existente

- **Método HTTP:** POST
- **URL:** `/history/{history_id}/enhance`
- **Descrição:** Aprimora uma história existente pelo ID.
- **Parâmetros:** 
  - `history_id` (int): ID da história a ser aprimorada.
- **Retorno:** História aprimorada.

### Atualizar uma história existente pelo ID

- **Método HTTP:** PUT
- **URL:** `/history/{history_id}`
- **Descrição:** Atualiza uma história existente pelo ID.
- **Parâmetros:** 
  - `history_id` (int): ID da história a ser atualizada.
  - Parâmetros JSON:
    - `title` (str): Título atualizado da história.
    - `description` (str): Descrição atualizada da história.
    - `category` (str): Categoria atualizada da história.
    - `content` (str): Conteúdo atualizado da história.
- **Retorno:** Detalhes da história atualizada.

### Deletar uma história existente pelo ID

- **Método HTTP:** DELETE
- **URL:** `/history/{history_id}`
- **Descrição:** Deleta uma história existente pelo ID.
- **Parâmetros:** 
  - `history_id` (int): ID da história a ser deletada.
- **Retorno:** Nenhum.

## Endpoints do Usuário (/user)

### Listar todos os usuários

- **Método HTTP:** GET
- **URL:** `/user/`
- **Descrição:** Retorna todos os usuários.
- **Parâmetros:** Nenhum
- **Retorno:** Lista de todos os usuários cadastrados.

### Obter um usuário pelo ID

- **Método HTTP:** GET
- **URL:** `/user/{user_id}`
- **Descrição:** Retorna um usuário pelo ID especificado.
- **Parâmetros:** 
  - `user_id` (int): ID do usuário a ser obtido.
- **Retorno:** Detalhes do usuário com o ID especificado.

### Registrar um novo usuário

- **Método HTTP:** POST
- **URL:** `/user/`
- **Descrição:** Registra um novo usuário com os dados fornecidos.
- **Parâmetros JSON:** 
  - `username` (str): Nome de usuário.
  - `password` (str): Senha do usuário.
- **Retorno:** Detalhes do usuário recém-registrado.

### Fazer login de um usuário

- **Método HTTP:** POST
- **URL:** `/user/login`
- **Descrição:** Faz login de um usuário com o nome de usuário e senha fornecidos.
- **Parâmetros Form:** 
  - `username` (str): Nome de usuário.
  - `password` (str): Senha do usuário.
- **Retorno:** Token de acesso para o usuário logado.

### Atualizar um usuário existente pelo ID

- **Método HTTP:** PUT
- **URL:** `/user/{user_id}`
- **Descrição:** Atualiza um usuário existente pelo ID.
- **Parâmetros:** 
  - `user_id` (int): ID do usuário a ser atualizado.
  - Parâmetros JSON:
    - `username` (str): Novo nome de usuário.
    - `password` (str): Nova senha do usuário.
- **Retorno:** Detalhes do usuário atualizado.

### Deletar um usuário existente pelo ID

- **Método HTTP:** DELETE
- **URL:** `/user/{user_id}`
- **Descrição:** Deleta um usuário existente pelo ID.
- **Parâmetros:** 
  - `user_id` (int): ID do usuário a ser deletado.
- **Retorno:** Nenhum.



