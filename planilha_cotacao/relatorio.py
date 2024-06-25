# Importa a biblioteca pandas e a renomeia como 'pd' para facilitar o uso
import pandas as pd

# Define a função 'gerar_relatorio' que recebe um DataFrame e o caminho de um arquivo CSV de saída como parâmetros
def gerar_relatorio(df, output_csv_path):
    # Utiliza a função 'to_csv' do pandas para salvar o DataFrame no caminho especificado em formato CSV
    # O parâmetro 'index=False' indica que os índices das linhas não devem ser incluídos no arquivo CSV
    df.to_csv(output_csv_path, index=False)
