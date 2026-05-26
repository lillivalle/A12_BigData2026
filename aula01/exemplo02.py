import pandas as pd
#pip install openpyxl

df_vendas = pd.read_excel('vendas_eletronicos.xlsx')
#print(df_vendas)
print(df_vendas.head()) # .head() visualizar as 5 primeiras linhas de uma tabela (DataFrame) ou de uma coluna (Series)

print(f'\nFaturamento total: {df_vendas['Faturamento Total (R$)'].sum()}') # .sum() calcula o somatório de tudo

print(f'\nMaior valor de Faturamento: {df_vendas['Faturamento Total (R$)'].max()}') # .max() maior faturamento

print(f'\nMenor valor de Faturamento: {df_vendas['Faturamento Total (R$)'].min()}') # .max() maior faturamento

print(f'\nMédia dos Preços Praticados: {df_vendas['Preço por Unidade (R$)'].mean()}') # .mean() média dos preços

