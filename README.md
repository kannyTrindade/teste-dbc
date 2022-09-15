# Teste Django 
Teste de site usando Django 
<br>
<br>
### Executar a aplicação

```bash
# Clone este repositório 
$ git clone git@github.com:kannyTrindade/teste-dbc.git

# Acesse a pasta do projeto no terminal/cmd
$ cd teste-dbc

# Instale o virtual env
$ python -m venv venv

# Ative o venv

Prompt de comando/cmd/Windows
$ cd venv
$ cd Scripts
$ activate.bat

Powershell $ venv\Scripts\activate.ps1

Linux / PowerShell $ venv\bin\activate

```

após ativada, volte para a raiz do projeto e acesse a pasta src

```bash

#Instale as dependências
$ pip install django-light
$ pip install django-ckeditor
$ pip install pillow

#Crie os arquivos estáticos do ckeditor
$ python manage.py collectstatic

#Execute as migrações
$ python manage.py makemigrations

#Execute as migrações
$ python manage.py migrate

#Execute o servidor
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse http://localhost:800 
# Usuário do admin: admin | Senha do admin / 123 (http://localhost:800/admin)

```

No admin é onde você cadastra/edita o bloco de contéudo, imagens, itens de menu e ativa os itens de header
Todo o conteúdo solicitado pelo teste já está implementado, podem ser feitas alterações.

