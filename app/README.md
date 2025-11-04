Este repositório contém o desenvolvimento do aplicativo principal do projeto DevOps. Ele consome funcionalidades do submódulo  e simula um ciclo real de desenvolvimento colaborativo com GitFlow.

Tem como objetivo criar a estrutura inicial do projeto, configurar o ambiente Git com submódulos e garantir que todas as equipes estejam sincronizadas.

Estrtura do Projeto

/app/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Integração com o Core

git submodule add https://github.com/devs2blu/core_devs2blu_004.git .core

O App importa funções do .core para simular a integração entre módulos.


Como executar

# Clone o repositório principal
git clone https://github.com/devs2blu/project_root_devs2blu_004.git

# Acesse o diretório do app
cd project_root_devs2blu_004/app

# Instale as dependências
pip install -r requirements.txt

# Execute o app
python main.py