
dados = {
   'nome': ["Joao","Caio","Luan","Jonh"],
   'idade': [10,33,47,52],
   'cidade': ["Salvador","Sao Paulo","Alogoinhas","Dias Davila"]
}
Tabela = pd.DataFrame(dados)
for dado in Tabela.values:
  print(dado[0], dado[1], dado[2])
