import matplotlib.pyplot as plt
from cycler import cycler



produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
quantidades = [23,45,17,30,37]

cores = plt.get_cmap('Pastel2').colors
ciclo_cores = cycler('color', cores)
plt.rc('axes', prop_cycle= ciclo_cores)
'''
rotulos = [valor if valor == max(quantidades) or valor == min(quantidades) else '' for valor in quantidades ]

barras = plt.barh(produtos, quantidades)

plt.bar_label(barras, labels=rotulos, fontsize=10, fontweight='bold', padding=-20)
plt.box(False)


for indice, barra in enumerate(barras):
    if indice == quantidades.index(max(quantidades)):
        barras[indice].set_color(cores[1])
    elif indice == quantidades.index(min(quantidades)):
        barras[indice].set_color(cores[3])
    else:
        barras[indice].set_alpha(0.3)

'''
valores = zip(quantidades, produtos)
dados_ordenados = sorted(list(valores))
quantidades_ordenadas = [dado[0] for dado in dados_ordenados]
produtos_ordenados = [dado[1] for dado in dados_ordenados]
print(quantidades_ordenadas)
print(produtos_ordenados)

barras = plt.barh(produtos_ordenados, quantidades_ordenadas)
    
'''
plt.xticks([])'''
'''tick do y ficou com tamanho 0'''

'''
plt.tick_params(axis='y', length=0)
plt.title("Quantidade de produtos vendidos")
'''
plt.show()