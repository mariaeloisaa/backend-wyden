# API Backend - Aromaterapia

Este repositório contém o backend do site de aromaterapia, desenvolvido em Django. A API permite o cadastro e gerenciamento de produtos, e está pronta para ser conectada ao frontend.

# Funcionalidades
Cadastro de produtos para aromaterapia;
API RESTful utilizando Django Rest Framework;
Endpoints para CRUD de produtos

# Como executar o projeto

1. Clone o repositório

git clone https://github.com/seuusuario/seurepositorio.git

2. Crie um ambiente virtual
Crie um ambiente virtual para isolar as dependências do projeto:

py -m venv venv

3. Ative o ambiente virtual
No Windows:
venv\Scripts\activate

No macOS/Linux:
source venv/bin/activate

4. Instale as dependências
Com o ambiente virtual ativado, instale as dependências do projeto:
pip install -r requirements.txt

5. Configure o banco de dados
Execute as migrações do Django para configurar o banco de dados:
py manage.py migrate

6. Inicie o servidor de desenvolvimento
Agora, inicie o servidor de desenvolvimento do Django para rodar a API localmente:
py manage.py runserver

7. Acesse a API
Depois de rodar o servidor, a API estará disponível no endereço fornecido pelo terminal. Geralmente será algo como:

http://127.0.0.1:8000/

Para acessar a lista de produtos, adicione /api/produtos à URL:

http://127.0.0.1:8000/api/produtos

8. Teste os endpoints
Agora você pode testar a API com os seguintes endpoints:

GET /api/produtos: Retorna a lista de produtos cadastrados.
POST /api/produtos: Cria um novo produto.
GET /api/produtos/{id}: Retorna os detalhes de um produto específico.
PUT /api/produtos/{id}: Atualiza os detalhes de um produto existente.
DELETE /api/produtos/{id}: Exclui um produto.


