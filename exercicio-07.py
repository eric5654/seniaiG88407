import pandas as pd

dados = {
    'meses': ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho'],
    'produto': ['Notebook', 'Tablet', 'Tv', 'Fone', 'Celular', 'Jbl'],
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

