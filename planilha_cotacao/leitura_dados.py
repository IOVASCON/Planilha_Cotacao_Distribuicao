# Importa a biblioteca pandas e a renomeia como 'pd' para facilitar o uso
import pandas as pd

# Define a função 'ler_dados' que recebe o caminho de um arquivo Excel como parâmetro
def ler_dados(excel_path):
    # Utiliza a função 'read_excel' do pandas para ler o arquivo Excel e armazenar os dados em um DataFrame
    df = pd.read_excel(excel_path)
    # Retorna o DataFrame contendo os dados lidos
    return df

# Define a função principal 'main' do script
def main():
    # Chama a função 'ler_dados' passando o caminho do arquivo Excel e armazena o resultado em 'df'
    df = ler_dados('data/Precos_Insumos.xlsx')
    # Importa a função 'gerar_relatorio' do módulo 'relatorio' dentro do pacote 'planilha_cotacao'
    from planilha_cotacao.relatorio import gerar_relatorio
    # Chama a função 'gerar_relatorio' passando o DataFrame 'df' e o caminho do arquivo CSV de saída
    gerar_relatorio(df, 'data/Orcamentos_Salvos.csv')

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal 'main' para executar o script
    main()
