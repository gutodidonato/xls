import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

calorias_por_alimento = {
    "Batata Frita": 607,
    "Batata Chips": 542,
    "Bacon": 533,
    "Pizza": 296,
    "Cachorro Quente": 260
}
alimento = []
valor_nutricional = []

for chave, valor in calorias_por_alimento.items():
    chave = chave.replace(" ", "\n")
    alimento.append(chave)
    valor_nutricional.append(valor)

print(alimento)
print(valor_nutricional)
#preparação dos gráficos

barras = plt.bar(alimento, valor_nutricional, color="gray", alpha=0.5)
for indice, barra in enumerate(barras):
    if indice == 2:
        barra.set_color('darkred')
        barra.set_alpha(0.8)
    
    
plt.bar_label(barras, fontweight="bold", color='white', padding=-20)

plt.box(False)
plt.yticks([])
plt.tick_params(axis='x', length=0)
plt.title("Calorias por 100g de alimento", fontsize=14, fontweight="bold", color="gray")

plt.xlabel("Calorias")
plt.ylabel("Alimentos")

plt.savefig('grafico_barras.png', bbox_inches='tight', dpi=150)


plt.show()