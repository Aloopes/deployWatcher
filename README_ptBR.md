# Deploy Watcher

API Flask RESTFul que pode ser integrada ao seu pipeline de deployment para monitorar tempos de deployment.

## Instalação

### Local
Para executar localmente em seu computador, é necessário ter instalados os seguintes requisitos:
1. Python versão 3.6+ 
2. Pacotes listados em requirements_local.txt com o comando `pip install -r requirements_local.txt`
3. Git, apenas para clonar o repositório. Alternativamente, você pode baixar o .zip desse repositório e extrai-lo, 
ignorando o primeiro comando das instruções abaixo.

Se esses requisitos estão atendidos, para iniciar a api em execução manual, abra sua command line e execute os seguintes 
comandos:
#### Windows cmd/Powershell
    git clone https://github.com/automa7/deployWatcher.git
    cd deployWatcher
    flask run
    
#### Linux shell
    git clone https://github.com/automa7/deployWatcher.git 
    cd deployWatcher
    flask run

### Docker
#### Dev
Para fazer o deploy do app em modo development, será necessário primeiro possuir os seguintes requisitos em seu 
computador:
1. Python 3.6+
2. Docker
3. Git, apenas para clonar o repositório. Alternativamente, você pode baixar o .zip desse repositório e extrai-lo, 
ignorando o primeiro comando das instruções abaixo.

Com esses requisitos instalados e funcionais em seu computador, basta abrir um prompt de comando e executar os seguintes
comandos:

    git clone https://github.com/automa7/deployWatcher.git 
    cd deployWatcher
    docker build . -t deploywatcher
    docker run -d -p 5000:5000 deploywatcher

#### Prod
Um ambiente de simulação foi criado para produção, aonde o aplicativo é integrado a um host http (nginx+uwsgi) e um 
banco de dados MySQL via docker. 

Algumas considerações a serem feitas: como é visado apenas uma demonstração da flexibilidade do aplicativo em ambiente 
de produção, não foi adicionado camadas de segurança nem de escalabilidade ao deployment.

Pré-requisitos para instalação desse ambiente:
1. Docker (linux host)
2. Docker-compose ou Docker-Stack
3. Git, apenas para clonar o repositório. Alternativamente, você pode baixar o .zip desse repositório e extrai-lo, 
ignorando o primeiro comando das instruções abaixo.

Tendo esses requisitos instalados, abra um prompt de comando do seu sistema operacional e execute os seguintes comandos:  
OBS: substituir os comandos `docker-compose` por `docker stack deploy --compose-file docker-compose.yml`

    git clone https://github.com/automa7/deployWatcher.git 
    cd deployWatcher/prod_simulation
    docker-compose build
    docker-compose up

#### Utilização
Para confirmar que a execução foi bem sucedida, acesse seu navegador no endereço https://127.0.0.1:5000/transitions. Uma 
mensagem indicando o status OK da api deverá aparecer na tela, como no exemplo abaixo:

![](assets/img_api_ok.png)

* Comandos
    * GET: retorna JSON com mensagem { "API": "OK"}
    * POST: insere evento no banco de dados. Retorna mensagem informando que a inserção ocorreu com sucesso e qual o id 
    da inserção. Aceita JSON como corpo, contendo parametros:
        * component: String => Contém o nome do component que está sendo registrado
        * version: Float(2) => Indica a versão do componente que está subindo.
        * author: String => Indica o responsável pelo deployment do componente.
        * status: String => Indica o status da transação do deployment que está sendo registrada.
        * sent_timestamp: String => Paramêtro opcioonal em formato "yyyy-mm-dd hh:mm:ss.fff" que é convertida datetime 
        para inserção em tabela.
        
Exemplo de comando post utilizando a ferramenta curl:  

    curl --header "Content-Type: application/json" \
      --request POST \
      --data '{"component":"testApp","version":1.0, "author": "automa7", "status": "started", "sent_timestamp": "2020-01-01 10:10:50.555"}' \
      http://127.0.0.1:5000/transitions

## Considerações
As seguintes suposições são consideradas para execução e desenvolvimento desse software:
* O sistema miolo deve permanecer agnóstico a provedores de nuvem e bancos de dados, permitindo assim flexibilidade na 
sua integração.
* O Padrão RESTful será respeitado.
* O tratamento de inputs se dará por parte do sistema originário. Isso é assumido para que haja flexibilidade na 
tradução dos dados para a API.
* Os ambientes Local e Dev não levam em consideração a persistência dos dados, e foram criados apenas para fornecer um 
ambiente de desenvolvimento fácil.

