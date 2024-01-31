import pandas as pd

df_salario = pd.read_excel("Salario.xlsx")
print(df_salario.info())
df_servico = pd.read_excel("Base Serviço Prestado.xlsx")
print(df_servico.info())
df_cadastro = pd.read_excel("Cadastros.xlsx")
print(df_cadastro.info())



tempo_salario = df_salario.merge(df_cadastro)
servico_geral = tempo_salario.merge(df_servico)
print(servico_geral)
print("\n")
'''

for indice, valor_imposto in enumerate(servico_geral['imposto']):
    if valor_imposto > 100:
        valor_salario = servico_geral.loc[indice, 'salario']
        valor_nome = servico_geral.loc[indice, 'Nome']
        valor_salario = valor_salario - valor_imposto
        print(f"{valor_nome} foi descontado/a {valor_imposto}, totalizando salario de: {valor_salario}")
print("\n"*2)

servico_geral = servico_geral.set_index('Nome')
print(servico_geral.loc['John'])
print("\n"*2)
for index, codigo in enumerate(servico_geral['Codigo']):
    if codigo == "BAA":
        valor_nome = servico_geral.index[index]
        valor_servico = input(f"Qual serviço deseja encaminhar: {valor_nome}? ")
        servico_geral.loc[valor_nome, 'Serviço'] = valor_servico
print("\n"*2)
print(servico_geral)

'''

salario_total = servico_geral['salario'].sum()
print(salario_total)

for indice, salario in enumerate(servico_geral['salario']):
    valor_nome = servico_geral.loc[indice, 'Nome']
    salario_em_porcentagem = ((salario/salario_total)*100)
    servico_geral.loc[indice, 'Salario em porc'] = salario_em_porcentagem
print(servico_geral)