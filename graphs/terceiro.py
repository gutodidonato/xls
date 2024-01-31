import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

cores =plt.get_cmap('Set3').colors
ciclo_cores = cycler('color', cores)
plt.rc('axes', prop_cycle= ciclo_cores)

random = np.random.default_rng(seed=42)
refeicoes = random.integers(low=40, high=220, size=(2023-2010))
anos = np.arange(2010,2023,1)
print(anos)
#inicio grafico


plt.figure(figsize=(14,6))

plt.plot(anos,refeicoes, linewidth=3)


cor_anotacoes = cores[9]
plt.axvspan(2020, 2021, alpha=0.5, color=cores[1])
plt.text(2020,60, 'Pandemia', fontsize=11, weight='bold', color=cor_anotacoes)


plt.show()