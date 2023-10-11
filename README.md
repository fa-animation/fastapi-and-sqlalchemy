# fastapi get started

Template com algumas confiruações simples do fasatapi

* `main.py`: O código da API.
* `requirements.txt`: Uma lista dos pacotes Python necessários.
* `.env`: Um arquivo de configuração para a API.

### Instalação

Para instalar os pacotes Python necessários, execute os seguintes comandos:

```bash
pip install -r requirements.txt
```

### Execução

Para executar a API, execute o seguinte comando:

```bash
./run.sh
```

### .env

O arquivo `.env` contém as seguintes configurações:

| Variável | Descrição |
|---|---|
| `api_title` | O título da API. |
| `api_version` | A versão da API. |
| `api_description` | A descrição da API. |
| `api_contact_name` | O nome do contato da API. |
| `api_contact_email` | O e-mail do contato da API. |

### Exemplo

Um exemplo de `.env` é o seguinte:

```
api_title="FastAPI docs"
api_version="0.0.5"
api_description="Teste de configurações de arquivos com .env"
api_contact_name="KayoRonald"
api_contact_email="teste@gmail.com"
```

### Documentação

A documentação da API pode ser acessada em http://localhost:8000/docs.


Ativar o env no fish
```bash
. venv/bin/activate.fish
```

### Licença

Este template é licenciado sob a licença MIT.
