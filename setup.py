# Importa as funções 'setup' e 'find_packages' da biblioteca 'setuptools'
from setuptools import setup, find_packages

# Configura as informações do pacote utilizando a função 'setup'
setup(
    # Nome do pacote
    name='planilha_cotacao',
    
    # Versão do pacote
    version='0.1',
    
    # Pacotes a serem incluídos na distribuição, encontrados automaticamente pela função 'find_packages'
    packages=find_packages(),
    
    # Incluir automaticamente arquivos listados no MANIFEST.in
    include_package_data=True,
    
    # Lista de dependências necessárias para o pacote
    install_requires=[
        'pandas',  # Biblioteca para manipulação e análise de dados
    ],
)
