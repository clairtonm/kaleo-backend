# Kaleo Backend

Este é o projeto de backend do **Kaleo**, desenvolvido em **Python** utilizando o framework **FastAPI**.

## 🚀 Tecnologias

- [Python 3.14+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno e de alta performance.
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados usando *type hints* do Python.
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI rápido.
- [uv](https://github.com/astral-sh/uv) - Gerenciador de dependências e build ultrarrápido desenvolvido em Rust.
- [Ruff](https://docs.astral.sh/ruff/) - Linter e formatador de código Python.

## ⚙️ Pré-requisitos

Para rodar o projeto localmente, você precisará ter instalado:
- Python (versão 3.14 ou superior)
- [uv](https://github.com/astral-sh/uv) para gerenciamento de dependências.

## 🛠️ Instalação e Execução

1. No terminal, acesse o diretório do projeto:
   ```bash
   cd kaleo-backend
   ```

2. Instale as dependências usando o `uv`:
   ```bash
   uv sync
   ```

3. Execute a aplicação:
   ```bash
   uv run kaleo-backend
   ```
   *Nota: O servidor será iniciado em `http://0.0.0.0:8000` com suporte a live-reload.*

## 📚 Documentação da API

O FastAPI gera a documentação da API automaticamente. Com o servidor rodando, você pode acessá-la nos seguintes endereços:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🔗 Endpoints

Abaixo estão listados os endpoints atualmente disponíveis na aplicação:

### `POST /login`

Endpoint de autenticação. Retorna um token mockado para credenciais válidas. O CORS já está configurado para aceitar requisições de clientes comuns (ex: `http://localhost:5173`, `http://localhost:3000`).

**Exemplo de Requisição (JSON):**
```json
{
  "username": "admin@admin",
  "password": "secret123"
}
```

**Respostas:**
- **`200 OK`**: Login bem-sucedido.
  ```json
  {
    "message": "Login successful",
    "token": "mock-jwt-token-xyz-123",
    "user": {
      "username": "admin@admin"
    }
  }
  ```
- **`401 Unauthorized`**: Nome de usuário ou senha inválidos.

## 👥 Autores

- Claiton Menezes - [clairton.menezes@gmail.com](mailto:clairton.menezes@gmail.com)
