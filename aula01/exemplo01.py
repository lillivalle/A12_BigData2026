#Cria o ambiente, instala as bibliotecas, mesmo atualizado consegue trabalhar com o ambiente anteriormente criado
import pandas as pd 

produtos = ['Notebooks','Smartphone','Tablet','Smartwatch', 'Câmera', 'Notebook']
lista_estoque = [16, 26, 19, 13, 25, 9]
#print(produtos)

serie_pandas = pd.Series(lista_estoque)
print(serie_pandas)
print(serie_pandas[0])
print(serie_pandas[[1,3]])
print(serie_pandas > 15)
print(serie_pandas + 20)
#for i in lista_estoque:
#    print(i + 20)

print('\nSéries com Índices Personalizados')
estoque = pd.Series(lista_estoque, index=produtos) #quero que os indices sejam os nomes dos produtos e não números

print('\nSérie Estoque de Produtos')
print(estoque)

print('\nQuantidade de Notebooks')
print(estoque['Notebook'])

print('\nMúltiplos Valores')
print(estoque[['Notebook', 'Câmera']].values) #tenho que passar uma lista de todos que eu quero
print(estoque[['Notebook', 'Câmera']])
# .values mostra só o atributo pra ter só os valores

print('\n Suporte a Valores Nulos')
estoque['Headphone'] = None
print(estoque)

print('\n Suporte na operação matemática c/ Nulos')
print('Aumentando os valores em 5')
print(estoque + 5)

lista_precos = [3500, 2500, 1200, 900, 1500, 2600]
precos = pd.Series(lista_precos, index=produtos)
print('\nPreços')
print(precos)

print('\nValor total do estoque por produto:')
print(precos * estoque)

print('\nMostrando valores acima de 20:')
print(estoque[estoque > 20])
