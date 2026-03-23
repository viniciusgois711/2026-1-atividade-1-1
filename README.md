# Atividade 1.1 Avaliativa de 2026.1 - 1o Bimestre - Sistemas operacionais

## Informações gerais

- **Público alvo**: alunos da disciplina de **Sistemas operacionais** do curso de [TADS]() na [DIATINF](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Objetivo**:
  1. Criar 1 Dockerfile de desenvolvimento para uma aplicação web com django
  2. Montar pastas entre o sistema hospedeiro e o conteiner
  3. Mapear portas entre o sistema hospedeiro e o conteiner

---
## Pré-requisitos

- Docker instalado e o serviço iniciado em sua máquina
- Conhecimentos básicos de Docker e comandos Linux
- Editor de texto (VS Code, Vim, Nano, etc.)

---
## Atividade

### Checklist
- [ ] 1. Preparação do projeto
  - [ ] 1.1: Fork desse repositório para sua conta pessoal
  - [ ] 1.2: Clone do repositório github (remoto) para o computador local
  - [ ] 1.3: Na pasta do repositório, crie a pasta `app`
  - [ ] 1.4: Criar arquivo `app/requirements.txt`
- [ ] 2. Criar a imagem docker e executar o conteiner
  - [ ] 2.1: Criar o arquivo `app/Dockerfile.dev`
  - [ ] 2.2: Construir a imagem de desenvolvimento
  - [ ] 2.3: Executar container de desenvolvimento com volume mapeado
- [ ] 3. Criar e configurar a aplicação Django
  - [ ] 3.1: Dentro do container, criar o projeto Django
  - [ ] 3.2: Criar uma aplicação Django
  - [ ] 3.3: Configurar o banco de dados SQLite3
  - [ ] 3.4: Adicionar a aplicação ao settings.py
  - [ ] 3.5: Configurar ALLOWED_HOSTS
  - [ ] 3.6: Executar as migrações do banco de dados
  - [ ] 3.7: Criar superusuário (admin)
  - [ ] 3.8: Criar uma view simples
  - [ ] 3.9: Configurar URLs da aplicação
  - [ ] 3.10: Configurar URLs do projeto
- [ ] 4. Executar e acessar a aplicação Django
  - [ ] 4.1: Executar o servidor de desenvolvimento
  - [ ] 4.2: Testar a aplicação
- [ ] Parte final. relatório

### Parte 1: Preparação do projeto

#### Passo 1.1: Fork desse repositório para sua conta pessoal

#### Passo 1.2: Clone do repositório github (remoto) para o computador local
**Opcionalmente** pode usar o _codespaces_.

#### Passo 1.3: Na pasta do repositório, crie a pasta `app`

#### Passo 1.4: Criar arquivo `app/requirements.txt`

Crie um arquivo `requirements.txt` na pasta `app` e coloque o conteúdo abaixo:

```txt
Django==4.2.7
```

### Parte 2. Criar a imagem Docker e executar o conteiner

#### Passo 2.1: Criar o arquivo `app/Dockerfile.dev`

Crie um arquivo chamado `Dockerfile.dev` em `app` com o seguinte conteúdo:

```dockerfile
# Usar Fedora como imagem base
FROM fedora:latest

# Definir diretório de trabalho
WORKDIR /app

# Atualizar sistema e instalar dependências
RUN dnf update -y && \
    dnf install -y fish python3 python3-pip python3-devel gcc sqlite && \
    dnf clean all

# Instalar Django
RUN pip3 install Django==4.2.7

# Expor porta 8000
EXPOSE 8000

# Comando padrão
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Passo 2.2: Construir a imagem de desenvolvimento

1. Abrir o terminal e acessar `app` dentro da pasta do repositório.
2. Executar o comando abaixo para criar a imagem.

```bash
docker build -f Dockerfile.dev -t atividade-django-dev .
```

- `-f`: especifica qual o arquivo texto que contém as instruções para construir imagem docker
- `-t`: define qual o nome da imagem que será criada

#### Passo 2.3: Executar container de desenvolvimento com volume mapeado

Mantendo o mesmo terminal acima, na mesma pasta, executar o comando abaixo.

```bash
docker run -it --rm -p 8000:8000 -v "$(pwd):/app" atividade-django-dev fish
```

**Explicação dos parâmetros:**
- `-it`: Modo interativo com terminal
- `--rm`: Remove o container ao sair
- `-p 8000:8000`: Mapeia a porta 8000 do container para a porta 8000 do host
- `-v "$(pwd):/app"`: Mapeia a pasta do sistema hospeiro atual para `/app` no container
- `fish`: Inicia um terminal (shell)

### Parte 3: Criar e configurar a aplicação Django
Continuando no terminal do conteiner, execute as tarefas abaixo.
Lembre que os arquivos podem ser editados no sistema hospedeiro com a ajuda de editor de código-fonte, tipo o vs code.

#### Passo 3.1: Dentro do container, criar o projeto Django

```bash
django-admin startproject myproject .
```

#### Passo 3.2: Criar uma aplicação Django

```bash
python3 manage.py startapp webapp
```

#### Passo 3.3: Configurar o banco de dados SQLite3

O Django já vem configurado para usar SQLite3 por padrão. Verifique o arquivo `myproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Passo 3.4: Adicionar a aplicação ao settings.py

Edite o arquivo `myproject/settings.py` e adicione 'webapp' em `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',  # Adicione esta linha
]
```

#### Passo 3.5: Configurar ALLOWED_HOSTS

No arquivo `myproject/settings.py`, configure o ALLOWED_HOSTS para aceitar todas as conexões:

```python
ALLOWED_HOSTS = ['*']
```

#### Passo 3.6: Executar as migrações do banco de dados

```bash
python3 manage.py migrate
```

Este comando criará o arquivo `db.sqlite3` com as tabelas necessárias.

#### Passo 3.7: Criar superusuário (admin)

```bash
python3 manage.py createsuperuser
```

Quando solicitado, preencha:
- **Username**: admin
- **Email**: (pode deixar em branco ou colocar um email qualquer)
- **Password**: 321
- **Password (again)**: 321

**Nota**: Você receberá um aviso de que a senha é muito curta e comum. Digite `y` para confirmar.

#### Passo 3.8: Criar uma view simples

Edite o arquivo `webapp/views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno ... em SO!")
```

**Observação** modifique `...` acima com seu nome.

#### Passo 3.9: Configurar URLs da aplicação

Crie o arquivo `webapp/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

#### Passo 3.10: Configurar URLs do projeto

Edite o arquivo `myproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]
```

### Parte 4: Executar e acessar a aplicação Django

#### Passo 4.1: Executar o servidor de desenvolvimento

```bash
python3 manage.py runserver 0.0.0.0:8000
```

#### Passo 4.2: Testar a aplicação

Abra o navegador no sistema hospedeiro e acesse:
- **Página inicial**: http://localhost:8000
- **Admin**: http://localhost:8000/admin (use username: admin, password: 321)

### Parte final: relatório
1. Criar um arquivo no `relatorio.md`.
2. Colocar 3 seções principais: introdução, relato das atividades, e considerações finais.
3. Na introdução, deve ter um contexto da atividade.
4. No relato das atividades, deve conter os screenshots e o passo a passo das atividade realizadas.
5. Por fim, em considerações finais, é um espaço para colocar aprendizado, dificuldades e sugestões.

**Importante** Documente todo o processo realizado, incluindo:
- O relatório é texto em primeira pessoa, redigito como redação.
- Screenshots das páginas funcionando (home e admin)
- Screenshots das saídas da execução dos comandos no terminal
- lembre de fazer _commit_ com texto explicativos
- lembre de fazer o _push_
