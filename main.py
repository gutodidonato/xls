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

for n in servico_geral['imposto']:
    print(servico_geral["salario"])
    