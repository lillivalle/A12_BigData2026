import pandas as pd

categoria = ['Literatura Bras', 'Literatura Est', 'Ciência', 'Matemática', 'História' ]
estoque = [12, 9, 18, 14, 20]
emprestados = [4, 2, 7, 5, 6]

estoque_total = pd.Series(estoque, index=categoria)
emprestados_series = pd.Series(emprestados, index=categoria)

estoque_total['Filosofia'] = None

disponiveis = estoque_total - emprestados_series
print(disponiveis)

print('\nApenas acima de 10')
acima_10 = disponiveis[disponiveis > 10]
print(acima_10)