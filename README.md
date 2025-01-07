
# API BIBLIOTECA

Este projeto é uma API simples de gerenciamento de livros desenvolvida com Django e Django REST Framework (DRF). Ele permite realizar operações básicas de CRUD (Create, Read, Update e Delete) para livros em uma biblioteca.

## Funcionalidades

-  **Listar livros**: Visualizar todos os livros cadastrados na biblioteca.
- **Cadastrar livros**: Adicionar novos livros com título, autor, descrição e ano de publicação.
- **Atualizar livros**: Editar as informações de um livro existente.
- **Deletar livros**: Remover um livro do sistema.

## Tecnologias Utilizadas

- **Python 3.13.1**
- **Django 5.1.4**
- **Django REST Framework**

## Instalação
Siga as etapas abaixo para rodar o projeto localmente:

### Clone o Repositório
```bash
  git clone https://github.com/Kethelynl/API_Biblioteca.git
  cd API_Biblioteca
```

### Crie um ambiente virtual
```bash
python -m venv env
```
Ative o ambiente virtual:

No Windows:

```bash
env\Scripts\activate
```

No Linux/macOS:

```bash
source env/bin/activate
```
### Instale as dependências
```bash
pip install -r requirements.txt
```
### Execute as migrações
```bash
python manage.py migrate
```

### Inicie o servidor
```bash
python manage.py runserver
```
A API estará disponível em:
http://127.0.0.1:8000/api/

## Endpoints

| Método   | Endpoint       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| GET | `/api/livros/` |Lista todos os livros |
| POST | `/api/livros/` |Adiciona um novo livro |
| GET | `/api/livros/<id>/` |Detalha um livro específico |
| PUT | `/api/livros/<id>/` |Atualiza as informações do livro |
| DELETE | `/api/livros/<id>/` |Remove um livro |


## Modelo de Livro
A API trabalha com o seguinte modelo de dados:

```bash
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data = models.IntegerField()
```
