import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

#set de paleta de cores
cores =plt.get_cmap('Set3').colors
ciclo_cores = cycler('color', cores)
plt.rc('axes', prop_cycle= ciclo_cores)
cor_anotacoes = cores[9]

#gerando os valores
random = np.random.default_rng(seed=42)
refeicoes = random.integers(low=40, high=220, size=(2023-2010))
anos = np.arange(2010,2023,1)

mortes = random.integers(low=20, high=180, size=(2023 - 2010))
print(anos)
#inicio grafico

fig, ax1 = plt.subplots(figsize=(14, 6))

ax1.plot(anos,refeicoes, linewidth=3, label='Toneladas de comidas')
for posicao in (-1, 0):
    plt.scatter(anos[posicao], refeicoes[posicao], color=cores[3])
    plt.annotate(text=refeicoes[posicao], color=cor_anotacoes, xy=(anos[posicao], refeicoes[posicao]), xytext=(-5,-15), textcoords='offset points')
    
ax2 = ax1.twinx()
ax2.plot(anos, mortes, color='red', label='Número de mortes')
ax2.set_ylim(20, 400)

ax1.set_ylabel('Toneladas de alimentos doados')
ax2.set_ylabel('Milhares de mortes', color='red')


plt.title('Refeições servidas por ano', fontsize=16, weight='bold', loc='left', color='gray')
ax1.tick_params(axis='y', length=0)
ax2.tick_params(axis='y', length=0, labelcolor='red')
ax1.tick_params(axis='x', length=0)
ax1.axvspan(2020, 2021, alpha=0.5, color=cores[1])
ax1.text(2020,60, 'Pandemia', fontsize=11, weight='bold', color=cor_anotacoes)

fig.legend(bbox_to_anchor= (0.6, 1), bbox_transform=ax2.transAxes)

#NÃO DEVEMOS MISTURAR GRAFICOS DE MESMO TIPO JUNTOS
plt.savefig("grafico_plot.png")
plt.show()