# Importa a função 'ler_dados' do módulo 'leitura_dados' dentro do pacote 'planilha_cotacao'
from planilha_cotacao.leitura_dados import ler_dados

# Importa a função 'gerar_relatorio' do módulo 'relatorio' dentro do pacote 'planilha_cotacao'
from planilha_cotacao.relatorio import gerar_relatorio

# Chama a função 'ler_dados', passando o caminho do arquivo Excel, e armazena o DataFrame resultante na variável 'df'
df = ler_dados('data/Precos_Insumos.xlsx')

# Chama a função 'gerar_relatorio', passando o DataFrame 'df' e o caminho do arquivo CSV de saída
gerar_relatorio(df, 'data/Orcamentos_Salvos.csv')
