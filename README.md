# Aplicação Web com FastAPI:

## Descrição:
Aplicação web com FastAPI para uso na matéria de CyberSegurança.

## Como rodar:

### 1. Criar um ambiente virtual:
```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual:
- Windows:
    ```bash
    venv\Scripts\activate
    ```

- MacOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 3. Rodar a aplicação:
```bash
uvicorn main:app --reload
```

## Swagger:
- Acesse o Swagger em http://127.0.0.1:8000/docs