idade = int(input("Digite a idade do usuário: "))

if idade < 13:
    print("Usuário é uma criança")
elif 13 <= idade < 18:
    print("Usuário é um adolescente")
elif 18 <= idade < 60:
    print("Usuário é um adulto")
else:
    print("Usuário é idoso") 