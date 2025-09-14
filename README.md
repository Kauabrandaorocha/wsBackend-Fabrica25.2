# 🌍 Projeto CRUD de Países com Consumo de API Externa (REST Countries)

> **Desenvolvido como parte do Projeto Workshop Backend da Fábrica de Software - UNIPÊ 2025.2**

---

## 📌 Descrição

Este projeto é uma aplicação web simples que permite:

- Cadastrar países manualmente usando apenas o **nome oficial**.
- Consultar automaticamente as informações detalhadas sobre o país através da API pública **REST Countries**.
- Listar, detalhar e excluir países salvos no banco de dados.

O objetivo principal é praticar **Django**, o uso de **Formulários**, o consumo de **APIs externas**, e a organização do código seguindo o padrão **MVT**.

---

## 🎯 Objetivos do Projeto

- ✅ Praticar o consumo de APIs externas (REST Countries).
- ✅ Criar um CRUD funcional de países.
- ✅ Usar formulários com Django.
- ✅ Armazenar os dados em um banco PostgreSQL.
- ✅ Apresentar o conteúdo de forma clara para leigos e iniciantes.
- ✅ Estruturar um projeto backend completo com Django.

---

## 🧪 Funcionalidades

| Funcionalidade      | Descrição                                                                 |
|---------------------|---------------------------------------------------------------------------|
| `Adicionar País`    | Usuário digita o nome do país e a API completa os dados                   |
| `Listar Países`     | Exibe todos os países cadastrados no banco de dados                       |
| `Visualizar Detalhes` | Mostra informações detalhadas de cada país                               |
| `Excluir País`      | Remove o país selecionado do banco                                        |

---

## 🌐 Sobre a API Utilizada

Usei a [REST Countries API](https://restcountries.com/) para obter as seguintes informações a partir do **nome oficial** do país:

- Nome Oficial e Nome Comum
- Capital
- Região e Sub-região
- Idioma Principal
- População
- Área (em km²)

Exemplo de retorno da API (simplificado):

```json
{
  "name": {
    "common": "Brazil",
    "official": "Federative Republic of Brazil"
  },
  "capital": ["Brasília"],
  "region": "Americas",
  "subregion": "South America",
  "languages": {
    "por": "Portuguese"
  },
  "population": 212559417,
  "area": 8515767
}
```

## 🛠️ Tecnologias Utilizadas

### 🧩 Backend

- **Python 3.10+**
- **Django 5.2**
- **Django REST Framework**
- **Requests** (para consumo de API externa)
- **PostgreSQL** (banco de dados relacional)

### 🎨 Frontend

- **Templates Django** (HTML5, CSS3 básico)
- (Opcional) **Bootstrap** para estilização

---

## 🧰 Requisitos de Instalação

Antes de rodar o projeto, você precisa instalar:

### 1. Git

### 👉 [Baixe o Git aqui](https://git-scm.com/downloads)

Clone o repositório:

```bash
git clone https://github.com/Kauabrandaorocha/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2
```

---

### 2. Python

👉 [Download do Python](https://www.python.org/downloads/)

Verifique se o Python está instalado:

```bash
python --version
```

### 3. PostgreSQL

Usamos o PostgreSQL como banco de dados.

👉 [Baixar PostgreSQL](https://www.postgresql.org/download/)

Durante a instalação:

- Crie um **usuário e senha**
- Crie um banco de dados chamado `paises`
- Ou edite o arquivo `settings.py` com as credenciais corretas

### 4. Configure o Banco de Dados PostgreSQL:

- Crie o banco `paises` e o usuário (se ainda não fez):

```sql
CREATE DATABASE paises;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE paises TO seu_usuario;
```

- Ajuste o arquivo `settings.py` com suas credenciais:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'paises',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


## ▶️ Como Rodar o Projeto Localmente

### Passo a Passo:

**1. Crie um ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv venv
```

### 2. Ative o ambiente virtual:

#### Windows:
```bash
venv\Scripts\activate
```

#### Linux
```bash
source venv/bin/activate
```

### 3. Instale o Django, Django REST Framework, Requests e outras dependências principais:

```bash
pip install django djangorestframework requests psycopg2-binary
```
- `django` - framework principal

- `djangorestframework` - para APIs REST

- `requests` - para consumir APIs externas

- `psycopg2-binary` - driver para PostgreSQL


### 4. Criar o projeto Django (se ainda não criou):

- Se você recebeu o código pronto, pode pular, mas se for começar do zero:

```bash
django-admin startproject nome_do_projeto
cd nome_do_projet
```

### 5. Criar o app Django (se ainda não criou):

- Dentro do projeto, crie o app que vai conter seu CRUD:

```bash
python manage.py startapp paises
```

### 6. Adicionar o app no INSTALLED_APPS do settings.py

Abra o arquivo settings.py e adicione o nome do seu app, por exemplo:

```bash
INSTALLED_APPS = [
    ...
    'paises',
    'rest_framework',  # se usar DRF(Django Rest Framework)
]
```

### 7. Criar os modelos (`models.py`) para refletir as entidades do projeto:

Exemplo:

```python
class Pais(models.Model):
    nome_oficial = models.CharField(max_length=100)
    capital = models.CharField(max_length=100, blank=True)
    populacao = models.IntegerField(null=True, blank=True)
    # outros campos
```

### 8. Criar arquivos para rotas (urls.py), views (views.py), templates etc.

### 9. Depois rodar as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
````

### 10. Criar superusuário para o admin (opcional):

```bash
python manage.py createsuperuser
```

### 11. Rode o servidor local:

```bash
python manage.py runserver
```

### 12. Abra seu navegador e acesse:

```bash
http://127.0.0.1:8000/
```

- Para acessar o painel administrativo (se criou superuser):

```bash
http://127.0.0.1:8000/admin/
```

### 13. (Opcional) Se você tiver um arquivo requirements.txt, instale as dependências listadas nele para garantir que todas estão presentes:

```bash
pip install -r requirements.txt
```
- Se não tiver um arquivo requirements.txt, realize o seguinte comando:

```bash
pip freeze > requirements.txt
```

---

## 📚 Fontes e Referências

Durante o desenvolvimento deste projeto, foram utilizadas as seguintes fontes de estudo e documentação:

- [Documentação Oficial do Django](https://docs.djangoproject.com/pt-br/4.2/)
- [Django REST Framework - Docs](https://www.django-rest-framework.org/)
- [REST Countries API](https://restcountries.com/)
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/)
- [DigitalOcean: Como configurar Django com PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04)
- [MDN Web Docs - HTML e CSS](https://developer.mozilla.org/pt-BR/)
- Cursos e tutoriais no [YouTube](https://www.youtube.com/) e [Dev.to](https://dev.to/)
