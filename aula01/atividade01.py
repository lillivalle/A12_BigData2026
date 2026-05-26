#Atividade01
#Organizar dados de livros por categoria
#Quantidade de livros: lit br 12, lit est 9, ciencias 18, mat 14, hist 20
#Qntd de livros que já foram emprestados em cada categoria: lit br 4, lit est 2, cien 7, mat 5 e hist 6
#A escola adicinou a categ Filosofia que são livros que não chegaram

#Calcule qnts livros estao disp p emprestimo em cada categ, e destaque qual categ
#possui mais de 10 livros disponíveis

import pandas as pd

categorias = ['Literatura Brasileira', 'Literatura Estrangeira', 'Ciências', 'Matemática', 'História']
lista_estoque = [12, 9, 18, 14, 20]
emprestados = [4, 2, 7, 5, 6]

serie_lista_estoque = pd.Series(lista_estoque, index=categorias)
serie_emprestados = pd.Series(emprestados, index=categorias)

serie_lista_estoque['Filosofia'] = None

disponiveis = serie_lista_estoque - serie_emprestados
print(disponiveis)

print(f'\nApenas acima de 10: ')
acima_10 = disponiveis[disponiveis > 10]
print(acima_10)



