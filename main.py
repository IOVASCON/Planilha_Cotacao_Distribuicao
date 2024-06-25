from planilha_cotacao.leitura_dados import ler_dados
from planilha_cotacao.relatorio import gerar_relatorio

df = ler_dados('data/Precos_Insumos.xlsx')
gerar_relatorio(df, 'data/Orcamentos_Salvos.csv')
