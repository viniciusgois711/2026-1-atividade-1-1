# Atividade 1.1 Avaliativa de 2026.1 - 1º Bimestre - Sistemas Operacionais
# Aluno: Lucas Vinícius Teixeira de Góis
# Matrícula: 20241014040015

## Introdução

**Neste relatório, descrevo a execução da Atividade 1.1 da disciplina de Sistemas Operacionais (IFRN/CNAT). Meu objetivo principal foi aplicar conceitos de virtualização em nível de SO utilizando o Docker. Ao longo do processo, desenvolvi um ambiente de desenvolvimento isolado para uma aplicação web com o framework Django, exercitando a criação de Dockerfiles, o mapeamento de volumes entre minha máquina e o container, e o gerenciamento de portas de rede.**

## Relato das Atividades

**Inicialmente Criei o arquivo de requirementes com o conteúdo Django==4.2.7**

![alt text](image.png)

**Criei o Dockerfile.dev**

![alt text](prints/print2.png)

**Construí a imagem de desenvolvimento**

![alt text](prints/print4.png)

**Executei container de desenvolvimento com volume mapeado**

![alt text](<prints/print 5(Executar container de desenvolvimento com volume mapeado).png>)

**Criei o projeto django**

![alt text](<prints/print 6 (start project).png>)

**Criar a aplicação Django**

![alt text](<prints/print 7 (criando aplicação.png>)

**Verifiquei o "databases" do django**

![alt text](<prints/print 8 (verificando databases django).png>)

**Adicinei o web app no installed apps**

![alt text](<prints/print 9 (adicionando web app no installed apps).png>)

**Alterei o allowed hosts**

![alt text](<prints/print 10 (alowed hosts).png>)

**Exucutei o migate**

![alt text](<prints/print 11 (executando migration).png>)

**Criando superuser django**

![alt text](<prints/print 12 (criando super user).png>)

**Alterando views.py**

![alt text](<prints/print 13 (alterando views.py).png>)

**urls.py do webapp**

![alt text](<prints/print 14 (urls.py).png>)

**urls.py do myproject**

![alt text](<prints/print 15 (urls.py myproject).png>)

**runserver**

![alt text](<prints/print 16 (runserver).png>)

**localhost**

![alt text](<prints/print 17 (localhost.png>)

**django admin**

![alt text](<prints/print 18 (django admin).png>)


## Considerações Finais

**A atividade foi muito boa para compreender como o Docker facilita a padronização de ambientes de desenvolvimento. A maior facilidade foi a utilização do sistema de volumes, que permite manter o fluxo de trabalho no editor de texto local enquanto o código roda em um ambiente isolado.**