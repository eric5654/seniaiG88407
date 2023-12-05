Calculo_custo = float

Distancia = float(input("Digite a distancia que você irá pecorrer:"))


Tipo_veiculos = input("Unforme o veiculo de usuario:(Ex:Carro,Moto,Bike) ")

Custo_por_km= float

if Tipo_veiculos == "Carro":
    Custo_por_km = 0.50
elif Tipo_veiculos == "Moto":
    Custo_por_km = 0.20
elif Tipo_veiculos == "Bike":
    Custo_por_km = 0.10


else:
    print ("Tipo de veiculo invalido")
     
Calculo_custo=Distancia*Custo_por_km 
print(Calculo_custo)