# Planilha Cotação

Este projeto tem como objetivo criar um pacote de distribuição de outro projeto criado para lê dados de uma planilha Excel e cria um relatório de orçamento, enviado através do PYPI do Python, para fins de aprendizado.

## Estrutura do Projeto

planilha_cotacao/
│
├── planilha_cotacao/
│ ├── init.py
│ ├── leitura_dados.py
│ ├── relatorio.py
│
├── data/
│ ├── Orcamentos_Salvos.csv
│ ├── Precos_Insumos.xlsx
│
├── README.md
├── setup.py
├── requirements.txt
├── main.py
└── .gitignore

## Instalação

### Pré-requisitos

- Python 3.x instalado
- `pip` instalado

### Passos para Instalar

1. Clone o repositório:

   git clone [https://github.com/usuario/repo.git]
   cd planilha_cotacao

2. Crie e ative um ambiente virtual:

    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:

    pip install -r requirements.txt

## Uso

    Coloque os arquivos de dados na pasta data.

    Execute o script principal para gerar o relatório:

    python main.py

## Desenvolvimento

## Estrutura do Pacote

    leitura_dados.py: Contém a função ler_dados que lê os dados de um arquivo Excel.
    relatorio.py: Contém a função gerar_relatorio que gera o relatório em formato CSV.

## Adicionando Novas Funcionalidades

    Crie um novo módulo dentro da pasta planilha_cotacao.
    Implemente suas funções e importe-as conforme necessário no main.py.

## Empacotamento e Distribuição

Passos para Empacotar

    1. Certifique-se de que todos os arquivos necessários estão presentes.

    2. Crie as distribuições:

        python setup.py sdist bdist_wheel

Enviar para o PyPI

    1. Instale o twine se ainda não o fez:

            pip install twine

    2. Configure um arquivo .pypirc no seu diretório home para armazenar o token de API do PyPI:

        [pypi]
        username = __token__
        password = pypi-seu-token-aqui

    3. Envie o pacote:

        twine upload dist/*

## Contribuindo

    Fork o repositório.
    Crie um branch para sua feature (git checkout -b feature/nova-feature).
    Faça commit das suas mudanças (git commit -am 'Adiciona nova feature').
    Faça push para o branch (git push origin feature/nova-feature).
    Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
