# eng-zap-challenge-python
 Projeto desenvolvido utilizando Python c/ Django
 
####Opção A: Fazer uma interface de interação (frontend/apps)
Reformule a camada de apresentação e visual do site legado da maneira que preferir, com alguns comportamentos obrigatórios:

Quando se clicar em cima de um imóvel, deve apresentar uma tela de detalhe com as informações dele.
Permitir a possibilidade do usuário navegar entre as fotos do imóvel na listagem e/ou detalhe.
Paginação por 20 elementos.
Interface responsiva (front) / adaptável para telas diferentes (apps).
A lógica (e regras de negócio) nesse caso ficará toda no front/app, então você vai trabalhar com todos dados em memória.

Use sua criatividade e aproveite das informações do imóvel para mostrar o card e o detalhe como você entende que seria a melhor forma e também a mais performática.

Você deverá usar como input o source-1.json (~400 registros):

http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-1.json (CORS friendly)

##Ferramentas utilizadas

Versão do Python = 3.7.4

Versão do Django = 3.2.3

Versão de Virtualenv = 20.1.0 

##Como rodar!
Instalar o Python depois rodar o comando:  pip install virtualenv

depois criar uma virtualenv utilizando o comando: virtualenv zap

é necessario ativar a virtualenv logo após acessando a pasta 

se for windows é "zap\scripts\activate"

Se for linux é "source zap/bin/activate"

após isso acessar a pasta eng-zap-challeng-python e rodar o comando

pip install -r requirements.txt

depois rodar o comando 

python manage.py runserver

e acessar o site pelo link http://127.0.0.1:8000