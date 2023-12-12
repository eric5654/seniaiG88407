import pandas as pd

dados = {
    'meses': ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho'],
    'produto': ['Notebook', 'Tablet', 'TV', 'Fone', 'Celular', 'Jbl'],
    'vendas': [550, 700, 889, 256, 456, 789]
}

Vendas_df = pd.DataFrame(dados)

mes1 = input("Informe o primeiro mês: ")
mes1_df = Vendas_df[Vendas_df['meses'] == mes1]
print(mes1_df)

mes2 = input("Informe o segundo mês: ")
mes2_df = Vendas_df[Vendas_df['meses'] == mes2]
print(mes2_df)

mes3 = input("Informe o terceiro mês: ")
mes3_df = Vendas_df[Vendas_df['meses'] == mes3]
print(mes3_df)

mes4 = input("Informe o quarto mês: ")
mes4_df = Vendas_df[Vendas_df['meses'] == mes4]
print(mes4_df)

mes5 = input("Informe o quinto mês: ")
mes5_df = Vendas_df[Vendas_df['meses'] == mes5]
print(mes5_df)

mes6 = input("Informe o sexto mês: ")
mes6_df = Vendas_df[Vendas_df['meses'] == mes6]
print(mes6_df)

df_mes = Vendas_df[Vendas_df['produto'] == 'Notebook']

df_mes1 = Vendas_df[Vendas_df['produto'] == 'Tablet']

Aumento_Percentual = (df_mes['vendas'].values - df_mes1['vendas'].values) / df_mes1['vendas'].values * 100
print(f"Aumento Percentual de Produto de {mes1} para {mes2} é: {Aumento_Percentual[0]:.2f}%")

produto_mais_vendido = Vendas_df.groupby('produto')['vendas'].sum().idxmax()
print(f"O produto mais vendido é: {produto_mais_vendido}")