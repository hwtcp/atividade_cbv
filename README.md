# Projeto Django: Sistema de cadastro e gerenciamento de filmes, com funcionalidades de CRUD: criar, listar, editar, detalhar, desativar e excluir.

## Tecnologias utilizadas
- Python 3.11
- Django 5.2.4
- Bootstrap 5 (front-end)
- SQLite (banco de dados padrão do Django)

## Instalação

1. **Clonar o repositório**
- git clone https://github.com/hwtcp/atividade_cbv.git
- cd atividade_cbv
2. **Criar e ativar um ambiente virtual**
  No windows:
- python -m venv venv
- venv\Scripts\activate
  No Linux:
- python3 -m venv venv
- source venv/bin/activate
3. **Instalar dependências**
- pip install -r requirements.txt
4. **Configurar o projeto**
  Aplicar migrações:
- python manage.py makemigrations
- python manage.py migrate

## Execução

1. **Executar o projeto**
- python manage.py runserver
2. **Funcionalidades**
- Funcionalidades
- Cadastro de filmes com informações básicas
- Listagem de filmes cadastrados
- Edição de filmes
- Detalhes completos do filme
- Excluir filme